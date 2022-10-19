import json
import time  # 获取当前时间
import re  # 正则

from queue import Queue  # 队列
import requests  # url请求
from threading import Thread

# 多线程优化步骤：首页链接放入队列-遍历队列-主方法开启多线程
class TengxunSpider:
    # 通过该链接返回得到招聘详情页链接
    def __init__(self):
        # 获取所有城市对应的 address
        url = "https://careers.tencent.com/tencentcareer/api/data/GetMultiDictionary?timestamp={}&language=zh-cn&type=Nationality,WorkPlace,OuterType,BG,PostAttr".format(
            str(int(time.time())))
        workPlace = requests.get(url).json()["Data"]["WorkPlace"]
        self.address = {}
        for i in workPlace:
            # 字典追加
            self.address[i["Name"]] = i["Code"]
        # 创建队列对象
        self.q = Queue()

    # 实现主要逻辑
    # def run(self):
    #     self.getDetailUrl_list()

    # 拼凑首页链接
    def getDetailUrl_list(self):
        # city_ipt = input('城市：')
        # job_ipt = input('工作岗位：')
        # page_ipt = int(input('爬取页数：'))
        city_ipt = '广州'
        job_ipt = 'python'
        page_ipt = 5
        cityId = -1
        detailUrl_list = []
        flag = 0
        for key, value in self.address.items():
            if city_ipt == key:
                cityId = value
                flag = 1
        if flag == 0:
            print('该城市找不到匹配数据,无法打印')
            return
        for pageIndex in range(1, page_ipt + 1):
            indexUrl = "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp={}&cityId={}&keyword={}&pageIndex={}&pageSize=10&language=zh-cn&area=cn".format(
                str(int(time.time())), cityId, job_ipt, pageIndex)
            detailUrl_list.append(indexUrl)
        self.url_in(detailUrl_list)
            # self.q.append()
            # self.getDetailUrl(detailUrl_list)

    # 数据放入队列
    def url_in(self, detailUrl_list):
        for i in detailUrl_list:
            self.q.put(i)

    # 获取招聘详情网页url
    def getDetailUrl(self):

        #遍历队列
        while not self.q.empty():
            detailUrl_list= self.q.get()
            print('detailUrl_list==',detailUrl_list)
            # for i in detailUrl_list:
            response = requests.get(detailUrl_list)
            # 处理PostURL中postId=0情况 相应内容转为json格式再读取相应字段值
            posts = response.json()["Data"]["Posts"]
            for i in posts:
                postId = i["PostId"]
                # 写入txt文档
                self.write_txt(postId)


    # 写入txt文档
    def write_txt(self, postId):
        # 获取详情页工作岗位/工作要求链接 !!!通过format()给{}传参
        url = "https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp={}&postId={}&language=zh-cn".format(
            str(int(time.time())), postId)
        recruitPostName = requests.get(url).json()["Data"]["RecruitPostName"]
        # 标题中的/替换为空格，避免读成路径
        RecruitPostName_finally = re.sub(r'/', ' ', recruitPostName)
        responsibility = requests.get(url).json()["Data"]["Responsibility"]
        requirement = requests.get(url).json()["Data"]["Requirement"]
        try:
            # a表示在文档追加内容，编码格式为utf-8
            f = open('./数据/' + RecruitPostName_finally + '.txt', 'a', encoding='UTF-8')
            f.write('\n工作岗位：\n')
            f.write(RecruitPostName_finally)
            f.write('\n工作职责：\n')
            f.write(responsibility)
            f.write('\n工作要求：\n')
            f.write(requirement)
            f.close()
        except Exception as e:
            print('错误信息==',e)
        print('写入完毕')

    def main(self):
        self.getDetailUrl_list()

        t_list=[]
        #开启3个多线程
        for i in range(3):
            t = Thread(target=self.getDetailUrl())
            t_list.append(t)
            t.start()

        for i in t_list:
            i.join()

if __name__ == "__main__":
    start = time.time()
    t = TengxunSpider()
    t.main()
    end = time.time()
    print('耗时：',end - start)

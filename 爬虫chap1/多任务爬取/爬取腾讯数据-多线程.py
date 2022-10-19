import time
from threading import Thread

import requests
import json
import re
from queue import Queue


class TenxunSpider:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
        self.address = {"深圳": 1, "北京": 2, "广州": 5, "上海": 3}
        self.url_list = []  # 用来放置url
        self.q = Queue()  # 存放url地址的队列

    def run(self):  # 实现主要逻辑
        # 1.获取所有符合地址和招聘信息链接
        url_jog_list = self.get_url_infom()
        # 2.发送请求，获取响应
        # self.parse_url(url_jog_list)

    def parse_url(self):
        while not self.q.empty():

            url = self.q.get()
            print('-多线程==',url)

            response = requests.get(url=url, headers=self.headers)
            data2 = json.loads(response.text)
            for i in data2["Data"]["Posts"]:
                # 构建新的url
                new_url1 = "https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp={}&postId={}&language=zh-cn".format(
                    str(int(time.time())), i['PostId'])
                response2 = requests.get(new_url1, headers=self.headers)
                data3 = json.loads(response2.text)
                name_data2 = data3["Data"]["RecruitPostName"]  # 获取标题
                res_bili_data3 = data3["Data"]["Responsibility"]  # 获取工作职责
                requirement_data3 = data3["Data"]["Requirement"]  # 获取岗位要求
                self.write_data(name_data2, res_bili_data3, requirement_data3)
            print('url==', url)
        # while True:
        #     if not self.q.empty():
        #         url=self.q.get()
        #         print(url)
        '''for url in url_jog_list:
            response = requests.get(url=url, headers=self.headers)
            data2 = json.loads(response.text)
            for i in data2["Data"]["Posts"]:
                # 构建新的url
                new_url1 = "https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp={}&postId={}&language=zh-cn".format(
                    str(int(time.time())), i['PostId'])
                response2 = requests.get(new_url1, headers=self.headers)
                data3 = json.loads(response2.text)
                name_data2 = data3["Data"]["RecruitPostName"]  # 获取标题
                res_bili_data3 = data3["Data"]["Responsibility"]  # 获取工作职责
                requirement_data3 = data3["Data"]["Requirement"]  # 获取岗位要求
                self.write_data(name_data2, res_bili_data3, requirement_data3)'''

    # 写入txt文档中
    def write_data(self, name_data2, res_bili_data3, requirement_data3):
        try:
            name_data2 = re.sub("/", "", name_data2)
            f = open("./数据/" + name_data2 + ".txt", "a+", encoding="UTF-8")
            f.write(name_data2)
            f.write("\n工作职责：\n")
            f.write(res_bili_data3)
            f.write("\n工作要求：\n")
            f.write(requirement_data3)
            f.close()
        except Exception as e:
            print(e)
        print("写入完毕...")

    def get_url_infom(self):
        # 1.提供用户输入，所在地址和招聘行业信息
        address = input("请输入您选择的地点：")
        job_info = input("请输入您选择的工作岗位方向：")
        page = input("您要查询多少页：")

        address_input = ""
        for key, value in self.address.items():
            if address == key:
                address_input = str(value)
        for i in range(1, int(page) + 1):
            url = "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp={}&cityId={}&keyword={}&pageIndex={}&pageSize=10&language=zh-cn&area=cn".format(
                str(int(time.time())), address_input, job_info, str(i))
            self.url_list.append(url)
        self.url_in()  # 写入队列
        # return url_list

    def url_in(self):
        for i in self.url_list:
            self.q.put(i)
        # self.parse_url()

    def main(self):
        url_job_list = self.get_url_infom()
        print(url_job_list)
        t_list=[]
        for i in range(3):
            t = Thread(target=self.parse_url())
            t_list.append(t)
            t.start()
        for i in t_list:
            i.join()


if __name__ == '__main__':
    start = time.time()
    ts = TenxunSpider()
    # ts.run()
    ts.main()
    end = time.time()
    print(end - start)

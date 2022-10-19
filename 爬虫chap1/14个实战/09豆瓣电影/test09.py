'''
入口：豆瓣电影网站-点击电影左上角电影tab-获取热门电影数据url：https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0
---涉及知识点：
1、url请求解析
2、爬取解析具体网页信息
3、去除字符串首尾空格：strip()
---TODO:
4、影评-网友评论(之后可试着爬取影评-进入下一级url)
5、txt内容大纲：
------电影名 评分------
1、剧情简介：**
2、评论：
id:个人评论
'''
import requests
import json
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Cookie': 'll="118297"; bid=bqasE8rQVXY; ap_v=0,6.0; __utmc=30149280; _vwo_uuid_v2=DBB87138AB0D0D08C7125C95E45EAEE79|595e3b517ab4e67f5774e2f30440c27e; __gads=ID=61ffef6a2e66f2a3-226e69f029c600b8:T=1614393034:RT=1614393034:S=ALNI_Mbcfg8OnAQTcTxQakvJ54hbe4Hrcw; dbcl2="205604620:yXKLPjHlLP8"; ck=4e-M; frodotk="a1480a68f32eee85e3d81f3ad98ccb8f"; __utma=30149280.1219593792.1612854096.1614391809.1614397900.3; __utmb=30149280.0.10.1614397900; __utmz=30149280.1614397900.3.3.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; push_doumail_num=0; push_noty_num=1'
}

url = 'https://movie.douban.com/j/search_subjects'
params = {
    'type': 'movie',
    'tag': '热门',
    'page_limit': '10',
    'page_start': '0'
}


def down(url):
    resp = requests.get(url=url, headers=headers).text
    return resp

def parse(url):
    resp = requests.get(url=url, params=params, headers=headers).json()
    print('resp==',resp)
    # print(resp.json())
    subjects = resp['subjects']
    for item in subjects:
        #电影标题
        title_movie = item['title']
        #电影详情链接
        url_movie = item['url']
        #电影评分
        rate_movie = item['rate']
        #获取网页源码
        html = down(url_movie)
        # print('url_movie==', url_movie)
        #创建bs4对象，方便使用select()、select_one()解析网页
        html_bs4 = BeautifulSoup(html, 'lxml')
        # 剧情简介
        related_info = html_bs4.select_one('#link-report>span').get_text()
        # 去除字符串首尾空格
        related_info_finally = related_info.strip()
        # print('related_info==',related_info.strip())
        # 短评-网友评论
        hot_comments = html_bs4.select('#hot-comments .comment')
        whole_comment = ''
        for i in hot_comments:
            # 网友id
            net_fri_name = i.select_one('h3 .comment-info a').get_text()
            # 网友评论内容
            comment_content = i.select_one('.comment-content .short').get_text()
            whole_comment += ('\n' + net_fri_name + ':\n' + comment_content + '\n')
        # print('title_movie==', title_movie)

        # print('whole_comment===', whole_comment)
        # open
        # 影评-网友评论(后头可试着爬取影评-进入下一级url)
        # movie_comments = html_bs4.select('#reviews-wrapper .main.review-item')
        # for j in movie_comments:
        #     # 网友id
        #     net_fri_name = j.select_one('.main-hd a').get_text()
        #     # 网友评论内容
        #     comment_content = j.select_one('.main-bd .short-content').get_text().strip()
        #
        #     print('影评net_fri_name===', net_fri_name + '\n' + comment_content)
        #写入文件 爬取数据文件夹自己创建，否则报错
        with open('./爬取数据/' + title_movie + '.txt', mode='w+', encoding='utf-8') as f:
            f.write('-' * 5 + '电影名称：' + title_movie + '  评分：' + rate_movie + '-' * 5)
            f.write('\n'+'1、剧情简介：\n')
            f.write(related_info_finally+'\n')
            f.write('\n'+'2、网友短评：')
            f.write(whole_comment)
    print('写入完成')


if __name__ == "__main__":
    parse(url)

'''
入口：豆瓣电影网站-点击电影左上角电影tab-获取热门电影数据url：https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0
---涉及知识点：
1、url请求解析
2、爬取具体网页信息
3、去除字符串首尾空格：strip()
---TODO:
4、影评-网友评论(之后可试着爬取影评-进入下一级url)
------电影名 评分------
剧情简介：**
评论：
id:个人评论
'''
import requests
import time
import random

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
}

for page in range(0,10):
    url = 'https://movie.douban.com/j/search_subjects'
    params = {
        'type': 'movie',
        'tag': '热门',
        'sort': 'recommend',
        'page_limit': '20',
        'page_start': page*20,
    }
    response = requests.get(url,params=params,headers=headers)
    print('params==',params)
    data = response.json()
    ls = data['subjects']
    print('len:',len(ls))
    for each in ls:
        rate = each['rate']
        print('rate:',rate)
        title = each['title']
        print('title:', title)
        url = each['url']
        print('url:', url)
        cover = each['cover']
        print('cover:', cover)
        id = each['id']
        print('id:', id)
        playable = each['playable']
        print('playable:', playable)
        print('='*200)
    time.sleep(random.random()+1)
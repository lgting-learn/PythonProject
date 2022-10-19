# import requests
# from lxml import etree
#
# url = 'https://s.weibo.com/top/summary?cate=realtimehot'
#
# headers = {
#     'User-Agent':'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'
# }
#
# def get(url):
#     response = requests.get(url, headers=headers)
#     if response.status_code ==200:
#         print("网页请求成功!")
#         parse(url)
#     else:
#         print('网页请求失败')
# def parse(url):
#     response = requests.get(url, headers=headers)
#     selector = etree.HTML(response.text)
#     number = selector.xpath('//td[@class="td-01 ranktop"]/text()')
#     topic = selector.xpath('//td[@class="td-02"]/a/text()')
#     hot = selector.xpath('//td[@class="td-02"]/span/text()')
#     for i in range(len(number)):
#         print(number[i], topic[i+1], hot[1])
#
# get(url)

import requests
import parsel
from lxml import etree

tieba_name = input('请输入贴吧名称：')
url = 'https://tieba.baidu.com/f?ie=utf-8&kw=%s&fr=search'%(tieba_name)
headers = {'User-Agent':'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}

response = requests.get(url=url, headers=headers)
html_data = response.text
# print(html_data)

html = parsel.Selector(html_data)
# print(html)
title_url = html.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href').extract()
print('title_url==',title_url)
for title in title_url:
    all_title = 'https://tieba.baidu.com'+title
    # print("当前帖子链接:", all_title)

    response_2 = requests.get(url=all_title, headers=headers).text
    #解析后才可以进行re,xpath,css匹配
    response_2_data = parsel.Selector(response_2)
    # print(response_2)
    img_url = response_2_data.xpath('//cc/div/img[@class="BDE_Image"]/@src').extract()
    # print(img_url)

    # for img in img_url:
    #     #content 获取字节流
    #     img_data = requests.get(url=img, headers=headers).content
    #     file_name = img.split('/')[-1]
          #wb+以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
    #     with open('img\\'+file_name, mode='wb+')as f:
    #         print('正在下载：', file_name)
    #         f.write(img_data)







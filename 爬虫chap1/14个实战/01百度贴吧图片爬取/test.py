#---涉及知识点：
# 1、遇到百度贴吧安全验证，无法正常获取页面源码：cookie
# 2、parsel.Selector()解析页面源码，才能进行xpath匹配
# 3、写入返回的页面源码，方便调试
# 4、获取要写入的二进制文件（图片）：requests.get(j.get()).content
# 5、打开文件：with open() as f:   不用f.close()

#---爬取步骤：
# 获取指定贴吧链接
# 发送requests请求网页源代码
# 解析响应内容
# for循环匹配链接，发送requests请求个人发布的帖子
# for循环，匹配图片，拼接图片链接
# 下载保存图片
import random

import requests
import parsel

# tiebaName = input('请输入贴吧名称：')
tiebaName='表情包'
url = "https://tieba.baidu.com/f?ie=utf-8&kw=%s&fr=search" % (tiebaName)
userAgents = ['Mozilla/5.0 (Windows NT 10.0; WOW64)']
#1、遇到百度贴吧安全验证，无法正常获取页面源码-解决：加上Cookie
headers = {'Cookie': 'BAIDUID=F37413809235CBE2CCE9336150F11AB5:FG=1; BDUSS=sxNmEzMDFpVE5LUzlBQ2tZclBtdVJtNGFJbUpIbFN6ZDdjcWhsQUlxZm9Mak5nSVFBQUFBJCQAAAAAAAAAAAEAAADsKK961LbJvbjfzKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOihC2DooQtgam; BDUSS_BFESS=sxNmEzMDFpVE5LUzlBQ2tZclBtdVJtNGFJbUpIbFN6ZDdjcWhsQUlxZm9Mak5nSVFBQUFBJCQAAAAAAAAAAAEAAADsKK961LbJvbjfzKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOihC2DooQtgam; BIDUPSID=F37413809235CBE2CCE9336150F11AB5; PSTM=1613277863; __yjs_duid=1_76304df19ebec569bb0b3d700b5a3bed1613902909554; Hm_lvt_7d6994d7e4201dd18472dd1ef27e6217=1613902909; Hm_lpvt_7d6994d7e4201dd18472dd1ef27e6217=1613902909; IS_NEW_USER=8ffe8aebe5088d41c8fcc66a; TIEBAUID=097ce01c5c8a1599d47f3255; ab_sr=1.0.0_Y2MxN2RlOWI4ZjNkOWI3MGNmZTk4NjJjNWE0ZDk5ZTU5Mzg3NWY3NDgzYTUzNWQ2ZDEwN2M2MjNmZmM5Y2UyNWZkZDg1NWRiN2IyNjcyZThhM2NiYTA2NzQ1OGE1MmU5NmJjZGFjY2I5YWFhNjFiMTMxYWUxOTY4ZDM2YmNmMTk=; st_data=491d6b9975e9cb6908628d9a476dfc3419ab3c4a51151e7470cda03f9f6dad70cc51f161a5e69e3c3ab6b736cafae70f9ff487858e9c3ac45be0d3c4c8526ac4417b901ff24ade86bc087440b676d4150d284cef8896bd9b14baf0eeb898e0f1328286aa0206741c94709d513baec86f88cde02ba53cee722854fc23357aa7bc; st_key_id=17; st_sign=a7770d6f; STOKEN=790ac5bb0eb39f3bf8592ab60327c6b91a7096e4be359a72257b92c06a4cc413; tb_as_data=4a64ada9035a25f725daf19e9abe08967db27282b4e39c8425ec3bf8f6b7d7673320d042d2d7a71ce30b2320535308ee00c4ac6246d88c2fc7374c44fffb35059456c7dc189133e0c08530963d9f1882c2d54580f303d69b6602f3e565fef738; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1613902915; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1613902915',
           'User-Agent':random.choice(userAgents)}
#2、解析页面源码，才能进行xpath匹配
url_html = parsel.Selector(requests.get(url=url, headers=headers).text)
#3、写入返回的页面源码，方便调试
# url_html_test = requests.get(url=url, headers=headers).content
# ff=open('./text.txt', mode='wb+')
# ff.write(url_html_test)
# ff.close()
print('url_html----',url_html)
child_url_html_all = url_html.xpath('//div[@class="threadlist_title pull_left j_th_tit "]//a//@href')
print('child_url_html_all===', child_url_html_all)
for i in child_url_html_all:
    url_item = 'https://tieba.baidu.com/' + i.get()
    response_item = requests.get(url_item)
    html_item = parsel.Selector(requests.get(url=url_item, headers=headers).text)
    html_item_img = html_item.xpath('//img[@class="BDE_Image"]//@src')
    print('html_item_img==', html_item_img)
    img_num = len(html_item_img)
    for j in html_item_img:
        #4、获取要写入的二进制文件（图片）
        response_img = requests.get(j.get()).content
        file_name = j.get().split('/')[-1]
        print('file_name==', file_name)
        #5、打开文件：with open() as f:   不用f.close()
        #wb+以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
        with open('./img/'+file_name, mode='wb+') as f:
            # print('共'+img_num+'个文件，正在下载第'+str(index)+'个：', file_name)
            print('共'+img_num+'个文件，正在下载：', file_name)
            f.write(response_img)





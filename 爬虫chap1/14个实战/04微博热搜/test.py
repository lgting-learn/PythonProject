
import requests
from lxml import etree
url='https://s.weibo.com/top/summary?cate=realtimehot'
headers = {
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
def get(url):
    if requests.get(url=url,headers=headers).status_code==200:
        parse(url)
        print('请求成功')
    else:
        print('请求失败',requests.get(url=url,headers=headers).status_code)


def parse(url):
    html=requests.get(url=url,headers=headers).content
    f=open('./test.txt','wb+')
    f.write(html)
    f.close()
    htmlxpath=etree.HTML(html)
    trs=htmlxpath.xpath('//tbody/tr')

    for tr in trs:
        order=tr[0].xpath('./text()')
        if len(order)>0:
            order=order[0]
        else:
            order='最热'
        # if()
        content=tr[1].xpath('./a//text()')[0]
        hot=tr[1].xpath('./span//text()')
        if len(hot) >0:
            hot = hot[0]
        else:
            hot='置顶'
        print('content==',order,content,hot)

get(url)
import requests
from lxml import etree
import time

url = 'https://weixin.sogou.com/weixin'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
}


def down(url):
    response = requests.get(url=url, headers=headers).content
    xpathObj = etree.HTML(response)
    # print('xpathObj',xpathObj)
    return xpathObj


def parse(url):
    params = {
        'query': '微星',
        'type': '2',
        'ie': 'utf8',
        's_from': 'input',
        '_sug_': 'n',
        'w': '01015002',
        'sut': '3300',
        'sst0': str(int(time.time())),
        'lkt': '0',
    }
    response = requests.get(url=url, params=params, headers=headers).content
    print(requests.get(url=url, params=params, headers=headers).text)

    htmlXpath = etree.HTML(response)
    itemArr = htmlXpath.xpath('//div[@class="txt-box"]')
    for i in itemArr:
        title_item = ''
        ppp_item = ''
        title = i.xpath('./h3/a//text()')
        for j in title:
            title_item += j
        ppp = i.xpath('./p[@class="txt-info"]//text()')
        for z in ppp:
            ppp_item += z
        print('pppp', title_item,ppp_item)


def get(url):
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        print('请求成功')
        parse(url)
    else:
        print('请求失败')


get(url)

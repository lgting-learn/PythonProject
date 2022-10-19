import requests
from bs4 import BeautifulSoup

url = 'http://www.shulou.la/4/4408/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}


def down(url):
    resp = requests.get(url=url, headers=headers).text
    return resp


def parse(url):
    resp = down(url)
    resp_bs4 = BeautifulSoup(resp, 'lxml')
    hrefArr = resp_bs4.select('.chapterlist>dd')
    hrefArr=hrefArr[10:]
    for i in hrefArr:
        resp = 'http://www.shulou.la'+i.select_one('a')['href']
        resp_bs4_item = BeautifulSoup(down(resp),'lxml')
        title = resp_bs4_item.select_one('#BookCon > h1').get_text()
        print('title==',title)
        content = resp_bs4_item.select_one('#BookText').get_text()
        print('content==',content)
        print('-'*500)



if __name__ == "__main__":
    parse(url)

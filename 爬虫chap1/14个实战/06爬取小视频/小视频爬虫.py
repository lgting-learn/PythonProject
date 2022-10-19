import requests
from bs4 import BeautifulSoup
import re
import time
import random


def down(url, params=None):
    '''
    下载给定url的内容
    :param url:
    :param params:
    :return:
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    }
    response = requests.get(url, params=params, headers=headers)
    html = response.text
    return html


def download_file(url):
    with requests.get(url, stream=True) as response:
        chunk_size = 1024
        content_size = int(response.headers['content-length'])
        path = './videoes/' + url.split('/')[-1]
        with open(path, 'wb') as file:
            n = 1
            for chunk in response.iter_content(chunk_size=chunk_size):
                loaded = n * 1024.0 / content_size
                file.write(chunk)
                print('已下载：{0:%}'.format(loaded))
                n += 1
    print('下载结束。。')


def parse(html):
    '''
    提取数据，下载视频
    :param html:
    :return:
    '''
    html = BeautifulSoup(html, 'lxml')
    ls = html.select('li.categoryem > div > a')
    print('len:', len(ls))
    base_url = 'https://www.pearvideo.com/'
    for each in ls:
        time.sleep(random.random())
        detail_url = base_url + each.get('href')
        print('detail_url:', detail_url)
        # 请求详情页面
        detail_html = down(detail_url)
        pat = re.compile(r'srcUrl="(.*?)"', re.S | re.M)
        match_obj = pat.search(detail_html)
        time.sleep(random.random())
        if match_obj != None:
            video_url = match_obj.group(1)
            print('video_url:', video_url)
            download_file(video_url)


if __name__ == "__main__":
    url = 'https://www.pearvideo.com/category_8'
    html = down(url)
    parse(html)

    # 异步请求的处理
    for page in range(1, 3):
        url = 'https://www.pearvideo.com/category_loading.jsp'
        params = {
            'reqType': 5,
            'categoryId': 8,
            'start': 12 * page
        }
        html = down(url,params=params)
        parse(html)









import requests
from lxml import etree
url = 'https://music.163.com/playlist?id=3212113629'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
}
def get_content(url):
    # 1.请求网站地址
    html = requests.get(url, headers=headers).content.decode('utf-8')
    f=open('./test.txt','wb+')
    f.write(requests.get(url, headers=headers).content)
    f.close()
    # print(html)
    tree = etree.HTML(html)
    """
    href="/song?id=1335466285"
    https://m701.music.126.net/20200824165238/b5ce9c3462c262fa5f5cc813b78a7baa/jdyyaac/010b/055d/010e/6ab216f4902717ce0baf6d082eb358f0.m4a
    """
    url_nusic = tree.xpath('//ul[@class="f-hide"]/li/a/@href')
    name = tree.xpath('//ul[@class="f-hide"]/li/a/text()')
    # print(url_nusic, title)
    for index, item in enumerate(url_nusic):
        url_id = item.split('=')[-1]
        print()
        file_name = name[index]
        print(url_id, file_name)
        music_base = 'http://music.163.com/song/media/outer/url?id=%s'%url_id
        print(music_base)
        file_path = '网易云歌曲/%s.mp3'%file_name

        with open(file_path, 'wb') as mu:
            req = requests.get(url=music_base, headers=headers)
            mu.write(req.content)





get_content(url)




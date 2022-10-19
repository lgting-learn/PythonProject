'''
---涉及知识点：
1、for循环中的异常处理
2、视频下载
'''
import requests

url = 'https://haokan.baidu.com/web/video/feed?tab=gaoxiao_new&act=pcFeed&pd=pc&num=20&shuaxin_id=1614413630513'
params = {
    'tab': 'gaoxiao_new',
    'act': 'pcFeed',
    'pd': 'pc',
    'num': '20',
    'shuaxin_id': '1614413630513'
}

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
    'cookie': 'BIDUPSID=4A734A94A884ABE38C0E61F206B2A986; PSTM=1595121359; BAIDUID=4A734A94A884ABE39D7735558DDC8854:SL=0:NR=10:FG=1; MCITY=-268%3A; BDUSS=VNYUWtjVWp3VDFsWHJxbFZ0MXlEUGx1dFZLdUdsOVZqazdWTVdldE5La0ZDMlJmRVFBQUFBJCQAAAAAAAAAAAEAAAAh6ILLzOy12zEyMzQ1Njc4OTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAV-PF8FfjxfU; BDUSS_BFESS=VNYUWtjVWp3VDFsWHJxbFZ0MXlEUGx1dFZLdUdsOVZqazdWTVdldE5La0ZDMlJmRVFBQUFBJCQAAAAAAAAAAAEAAAAh6ILLzOy12zEyMzQ1Njc4OTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAV-PF8FfjxfU; BDRCVFR[S4-dAuiWMmn]=I67x6TjHwwYf0; delPer=0; PSINO=2; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=1448_31660_32349_32045_32115_32090_32585_32482; PC_TAB_LOG=haokan_website_page; Hm_lvt_4aadd610dfd2f5972f1efee2653a2bc5=1598233632; Hm_lpvt_4aadd610dfd2f5972f1efee2653a2bc5=1598233632; reptileData=%7B%22data%22%3A%227e68084a981c714a75036158f5210b3116713e28f860873efcbce099030180bc4b2454fc6ef8045b52e1376acd4ce2648759b816dcdd4f8c7e2c73ea35f1a5398be2fb80809261b2c7cb5986f866c754ccb585fea3d7418146d253b889e71a24e5d17db8b63e79f667a0d7130d01bbe0ea900929dd457b17dd6520fae3e4bcbc%22%2C%22key_id%22%3A%2230%22%2C%22sign%22%3A%225efd0478%22%7D'

}

resp = requests.get(url=url, headers=headers)

def down(url):
    resp= requests.get(url=url,headers=headers).content
    return resp

def parse(url):
    resp_json = resp.json()
    videos = resp_json['data']['response']['videos']
    for i in videos:
        try:
            play_url = i['play_url']
            title = i['title']
        except:
            break
        down_mp4 = down(play_url)
        with open('./videos/'+title+'.mp4','wb') as f:
            f.write(down_mp4)
            print('正在下载：',title)

if resp.status_code == 200:
    parse(url)
    print('请求成功')
else:
    print('请求失败')

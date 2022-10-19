import requests
import re
from lxml import etree
url = 'https://weixin.sogou.com/pcindex/pc/pc_0/1.html'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
}
response = requests.get(url, headers=headers)

html = response.content.decode('utf-8')
# print(html)
# 文章标题
reg = r'<a uigs=".*?" href="(.*?)" target="_blank" data-share=".*?">(.*?)</a></h3>'
data = re.findall(reg, html)
print(data)
for item in data:
    print(item)
    captcha_url = item[0]
    title = item[1]
    r1 = requests.get(captcha_url, headers=headers).content.decode('utf-8')
    # 文章的内容
    html = etree.HTML(r1)

    content = html.xpath('//div[@id="js_content"]//p//text()')
    title = title.replace("?", "")
    title = title.replace("|", "")
    # print(content)
    # 文章下载
    if content:
        with open('./公众号文章/%s.txt' % title, mode='w', newline="", encoding='utf-8') as f:
            f.write("".join(content))
            f.write("\n")



















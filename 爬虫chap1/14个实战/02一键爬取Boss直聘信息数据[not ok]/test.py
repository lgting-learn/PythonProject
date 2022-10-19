import requests
import parsel
import json
job = 'python'
city_code = [{'name': '上海', 'code': '101020100'}]
url = 'https://www.zhipin.com/wapi/zpgeek/view/job/card.json?jid=a9e021b8eeeebffd1nR42ty6GFdT&lid=7FcD5qfrmdG.search.1&type=3'
headers = {
    'cookie': 'lastCity=101281600; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1613946872; __fid=4d5f40974351f2c75db5645b021d3510; __l=l=%2Fwww.zhipin.com%2Fc101020100%2F%3Fquery%3Dpython%26page%3D1%26ka%3Dpage-1&r=&g=&s=3&friend_source=0&s=3&friend_source=0; ___gtid=616123870; __c=1613946872; __a=42364025.1613946872..1613946872.23.1.23.23; __zp_stoken__=3878bZyopWWMQDUBGVGE2YnNhH2EeIRsrCWVaAy1zISBLFx8rITFoKgs9MUwhNiZhLVcSIDNxAyQCJiQkSXVBPyIQP3U6YTxFFH8NXG0gAXYOa3lHA0htWCUcCWUVKh5ZKwYYGSAODF92BW1HNA%3D%3D; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1613948919; __zp_sseed__=lAzdD223Ms1QYJSFI5ZHBGOZRKn1dOFubMvwYKfjj6Q=; __zp_sname__=f83bc67f; __zp_sts__=1613948923940',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64'
}
response = requests.get(url=url, headers=headers)
print('response==',response)

html = response.json()["zpData"]["html"]
print('html==',html)
href=html.xpath('//span[@class="job-name"]//a//@href')
html_test=response.content
f=open('html_test.txt', 'wb+')
f.write(html_test)
f.close()
print(href)

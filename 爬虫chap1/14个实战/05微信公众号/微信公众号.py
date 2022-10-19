'''
爬取微信公众号
---涉及知识点：
1、抓取二级页面-待补充
2、pymongo 连接mongodb数据库-待补充
'''
import requests
from lxml import etree
# import pymongo
import time
import random
import re


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
}

try:
    # # 数据库连接
    # server = 'localhost'
    # port = '27017'
    # dbname = 'admin'
    # user = 'admin'
    # pwd = '123'
    # uri = 'mongodb://'+user+':'+pwd +'@'+server + ":"+port +'/'+dbname
    # client = pymongo.MongoClient(uri)
    # # 指定数据库
    # mdb = client['dbwx']
    # # 指定集合
    # collec_wx = mdb['collec_wx_1908']
    #
    queries = ['微星','机械革命','炫龙','机械师','神州']
    for query in queries:
        #[1,2...10]
        for page in range(1, 11):
            print('query:', query, 'page:', page)
            #页面抓取
            params = {
                'oq': '',
                'query': query,
                '_sug_type_': 1,
                'sut': 0,
                'lkt': '0,0,0',
                's_from': 'input',
                'ri': 3,
                '_sug_': 'n',
                'type': 2,
                'sst0': int(time.time()*1000),
                'page': page,
                'ie': 'utf8',
                'p': '40040108',
                'dp': 1,
                'w': '01015002',
                'dr': 1,
            }
            url = 'https://weixin.sogou.com/weixin'
            response = requests.get(url,params=params,headers=headers)
            # 数据提取
            html = etree.HTML(response.content)
            ls = html.xpath('//ul[@class="news-list"]/li')
            print('len:',len(ls))
            for item in ls:
                title = item.xpath('.//h3/a//text()')
                title = ''.join(title)
                print('title:',title)
                detail_url = item.xpath('.//h3/a//@href')[0]
                print('detail url:',detail_url)
                summary = item.xpath('.//p[@class="txt-info"]//text()')
                summary = ''.join(summary)
                print('summary:',summary)
                source = item.xpath('.//a[@class="account"]/text()')
                if len(source)>0:
                    source = source[0]
                else:
                    source = '未知'
                print('source:',source)
                #timeConvert('1457143207')
                pub_date = item.xpath('.//span[@class="s2"]//text()')
                if len(pub_date)>0:
                    pat =re.compile(r"timeConvert\('(\d+)'\)")
                    pub_date = pub_date[0]
                    match_obj = pat.search(pub_date)
                    if match_obj != None:
                        timestamp  = int(match_obj.group(1))
                        date_obj = time.localtime(timestamp)
                        pub_date = time.strftime('%Y-%m-%d',date_obj)
                    else:
                        pub_date = '未知'
                else:
                    pub_date = '未知'
                print('pub_date:',pub_date)
                print('='*200)
                # 存储
            #     data = {
            #         'title':title,
            #         'detail_url': detail_url,
            #         'summary': summary,
            #         'source': source,
            #         'pub_date': pub_date
            #     }
            #     collec_wx.insert_one(data)
            # time.sleep(random.random()+1)

except Exception as e:
    print(e)

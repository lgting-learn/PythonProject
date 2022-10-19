import random

import scrapy

#发送post请求
class YoudaospiderSpider(scrapy.Spider):
    name = 'youdaospider'
    allowed_domains = ['fanyi.youdao.com']
    # start_urls = ['http://fanyi.youdao.com//']
    def start_requests(self):
        url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        UserAgents=[
            "Mozilla/5.0 (Linux; U; An\
            droid 8.1.0; zh-cn; BLA-AL00 Build/HUAW\
            EIBLA-AL00) AppleWebKit/537.36 (KHTML, l\
            ike Gecko) Version/4.0 Chrome/57.0.2987.13\
            2 MQQBrowser/8.9 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; U; An\
            droid 8.1.0; zh-cn; BLA-AL00 Build/HUAW\
            EIBLA-AL00) AppleWebKit/537.36 (KHTML, l\
            ike Gecko) Version/4.0 Chrome/57.0.2987.13\
            2 MQQBrowser/8.9 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; U; An\
            droid 8.1.0; zh-cn; BLA-AL00 Build/HUAW\
            EIBLA-AL00) AppleWebKit/537.36 (KHTML, l\
            ike Gecko) Version/4.0 Chrome/57.0.2987.13\
            2 MQQBrowser/8.9 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; U; An\
            droid 8.1.0; zh-cn; BLA-AL00 Build/HUAW\
            EIBLA-AL00) AppleWebKit/537.36 (KHTML, l\
            ike Gecko) Version/4.0 Chrome/57.0.2987.13\
            2 MQQBrowser/8.9 Mobile Safari/537.36"
        ]
        UserAgent=random.choice(UserAgents)
        #是:不是{"User-Agent",UserAgent}
        headers={"User-Agent":UserAgent}
        yield scrapy.FormRequest(
            url=url,
            headers=headers,
            formdata={
                "i": "hello",
                "from": "AUTO",
                "to": "AUTO",
                "smartresult": "dict",
                "client": "fanyideskweb",
                "salt": "16134693655973",
                "sign": "f40553749427ec0b801b07aa58da478c",
                "lts": "1613469365597",
                "bv": "3da01a09873456cfb5dba05f2124b148",
                "doctype": "json",
                "version": "2.1",
                "keyfrom": "fanyi.web",
                "action": "FY_BY_REALTlME",
            },
            callback=self.parse
        )
    def parse(self, response):
        print('有道 response',response)
        pass

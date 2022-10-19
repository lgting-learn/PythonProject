# -*- coding: utf-8 -*-
import scrapy
import random


class YoudaoSpider(scrapy.Spider):
    name = 'youdao'
    allowed_domains = ['fanyi.youdao.com']

    def start_requests(self):
        url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        UserAgents = [
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
        UserAgent = random.choice(UserAgents)

        # 构造请求头信息
        headers = {
            "User-Agent": UserAgent
        }
        yield scrapy.FormRequest(
            url = url,
            headers = headers,
            formdata={
                "i": "hell",
                "from": "AUTO",
                "to": "AUTO",
                "smartresult": "dict",
                "client": "fanyideskweb",
                "salt": "15930470321429",
                "sign": "952ac9d9b4b3d882f5ebb17e3e0acbe3",
                "ts": "1593047032142",
                "bv": "cc652a2ad669c22da983a705e3bca726",
                "doctype": "json",
                "version": "2.1",
                "keyfrom": "fanyi.web",
                "action": "FY_BY_REALTlME"
            },
            callback=self.parse
        )

    def parse(self, response):
        print(response)
        pass

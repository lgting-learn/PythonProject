import scrapy
import re
import pandas as pd
import numpy as np
np.set_printoptions(threshold=np.inf)

pd.set_option('display.width', 300) # 设置字符显示宽度
pd.set_option('display.max_rows', None) # 设置显示最大行
pd.set_option('display.max_columns', None) # 设置显示最大列，None为显示所有列
class WeibotestSpider(scrapy.Spider):
    name = 'weiboTest'
    allowed_domains = ['weibo.com']
    start_urls = ['https://s.weibo.com/top/summary?cate=realtimehot']

    # 处理一级url
    def parse(self, response):
        # 获取所有二级url
        url_child = response.xpath('//tr//td[@class="td-02"]//a')
        title_url = {}

        # print('url_child_title==',url_child_title)
        for url_single in url_child:
            new_url = 'https://s.weibo.com' + url_single.get()
            # new_title = re.sub("",url_single)
            print('+++++++++new_url==',url_single)
            yield scrapy.Request(new_url, callback=self.parse_item)

        pass

    # 处理每个二级url
    def parse_item(self, response):
        # 热门标题
        title = response.xpath('//div[@class="title"]//h1//a')
        # 评论者
        user_name = response.xpath('//div[@class="info"]//a//@nick-name')
        # print('--------------------------item=', title, user_name)
        # 爬取内容 进行截取
        pass

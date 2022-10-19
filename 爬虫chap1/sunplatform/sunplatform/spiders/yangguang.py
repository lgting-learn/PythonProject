# -*- coding: utf-8 -*-
import scrapy
from sunplatform.items import SunplatformItem


class YangguangSpider(scrapy.Spider):
    name = 'yangguang'
    allowed_domains = ['wz.sun0769.com']
    url_value = "http://wz.sun0769.com/political/index/supervise?page="
    url_index = 1
    start_urls = [url_value+str(url_index)]

    def parse(self, response):
        #取出每个帖子的子url
        web_url = response.xpath("//li//span//a[@target='_blank']/@href")
        for url in web_url:
            new_url = "http://wz.sun0769.com"+url.get()
            yield scrapy.Request(new_url, callback=self.parse_item)
        # 设置页码终止条件
        if self.url_index <= 40:
            self.url_index += 1
            yield scrapy.Request(self.url_value + str(self.url_index), callback=self.parse)

        pass
        # 处理每个帖子里

    def parse_item(self, response):
        #可以获取全部的url数据
        #创建自定对象
        item_dic = SunplatformItem()
        #存储字典
        item_dic["title"] = response.xpath("//p[@class='focus-details']")
        item_dic["content_ask"] = response.xpath("//div[@class='details-box']//pre")
        item_dic["content_answer"] = response.xpath("//div//pre[@style='margin: 0;']")
        yield item_dic
        pass

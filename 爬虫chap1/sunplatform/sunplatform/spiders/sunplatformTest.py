import scrapy
# sunplatform为项目名 SunplatformItem：类名
# 报红不影响程序运行
from sunplatform.items import SunplatformItem


class SunplatformtestSpider(scrapy.Spider):
    name = 'sunplatformTest'
    allowed_domains = ['wz.sun0769.com']
    url_value = "http://wz.sun0769.com/political/index/supervise?page="
    page = 1
    start_urls = [url_value + str(page)]

    # 本身相当于一个递归函数，不用写for循环实现单次循环逻辑，设置终止条件即可
    def parse(self, response):
        # print('阳光问政',response)
        # 获取第一页数据应该做的事情
        allowed_domains = self.allowed_domains[0]
        href = response.xpath("//li[@class='clear']//span[@class='state3']//a//@href")
        for i in href:
            url_all = 'http://' + allowed_domains + i.get()
            yield scrapy.Request(url_all, callback=self.parse_item)
            # print('阳光问政1==', url_all)
        # 设置终止条件：爬取几页数据
        if self.page <= 1:
            self.page += 1
            url_index = self.url_value + str(self.page)
            print('阳光问政2===', url_index)
            # yield加入队列
            yield scrapy.Request(url_index, callback=self.parse)
            pass

    # 处理子url逻辑：爬取内容
    def parse_item(self, response):
        # 创建字典对象
        item_dict = SunplatformItem()

        # 在items.py定义的变量对应这里的键值
        item_dict["title"] = response.xpath("//p[@class='focus-details']")
        item_dict["content_ask"] = response.xpath('//div[@class="details-box"]//pre')
        item_dict["content_answer"] = response.xpath('//div[@class="gf-reply mr-two"]//pre')
        yield item_dict

import scrapy


class MusicspiderSpider(scrapy.Spider):
    name = 'musicspider'
    #htqyy.com/去掉/
    allowed_domains = ['htqyy.com']
    start_urls = ['http://www.htqyy.com/genre/1']

    def parse(self, response):
        print('*****************')
        title_list = response.xpath("//li[@class='mItem']//span[@class='title']//a//@title")
        artist_name_list = response.xpath("//li[@class='mItem']//span[@class='artistName']//a//@title")
        album_name_lisy = response.xpath("//li[@class='mItem']//span[@class='albumName']//a//@title")
        play_count_list = response.xpath("//li[@class='mItem']//span[@class='playCount']")
        item_value = {}
        item_value['title_list'] = title_list
        item_value['artist_name_list'] = artist_name_list
        item_value['album_name_lisy'] = album_name_lisy
        item_value['play_count_list'] = play_count_list
        yield item_value
        # 拼接下次url
        page = int(response.url[-1]) + 1
        if page <= 5:
            print('page',page)
            next_url = response.url[:-1]+str(page)
            #self.parse没有()
            yield scrapy.Request(next_url,callback=self.parse)
        pass



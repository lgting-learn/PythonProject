# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import re#正则
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

#管道文件 对数据进行处理和保存
class MyscrapyPipeline:
    #定义初始化方法
    def __init__(self):
        self.f=open("音乐文件.txt",'w',encoding='UTF-8')

    def process_item(self, item, spider):
        num=len(item['title_list'])
        for i in range(num):
            title_list_str=item['title_list'][i].get()
            artist_name_list_str=item['artist_name_list'][i].get()
            album_name_lisy_str=item['album_name_lisy'][i].get()
            #收听人数获取到的是html 需要正则进行解析
            # <span class="playCount">41242人听过</span>
            play_count_list_str=item['play_count_list'][i].get()
            play_count_list_str=re.findall(r"\d+",play_count_list_str)[0]
            song_str=title_list_str+'  '+artist_name_list_str+'  '+album_name_lisy_str+'  '+play_count_list_str
            self.f.write(song_str+'\n')
            print(song_str+'正在保存...')
            print('管道',)
        self.f.write('----------------------------------\n')

        return item
    #提示爬取结束 固定写法
    def close_spider(self,spider):
        self.f.close()
        print('爬取结束')
        spider.crawler.engine.close_spider(spider,'done')



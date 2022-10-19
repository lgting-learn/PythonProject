# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re

class SunplatformPipeline:
    def __init__(self):
        self.f=open("阳光问政.txt","w",encoding='UTF-8')

    def process_item(self, item, spider):
        title_str = item["title"].get()
        content_ask_str=item["content_ask"].get()
        content_answer_str=item["content_answer"].get()
        #清洗数据 去除内容中的标签元素 获取文本内容
        title_str=re.sub('<p class="focus-details">|</p>',"",title_str)
        content_ask_str=re.sub('<pre>|</pre>',"",content_ask_str)
        content_answer_str=re.sub('<pre style="margin: 0;">|</pre>',"",content_answer_str)
        print('title_str==',title_str)
        print('content_ask_str==',content_ask_str)
        print('content_answer_str==',content_answer_str)
        self.f.write('\n---------------标题：\n')
        self.f.write(title_str)

        self.f.write('\n---------------问题：\n')
        self.f.write(content_ask_str)

        self.f.write('\n---------------官方回复：\n')
        self.f.write(content_answer_str)

        return item

    #提示爬取结束 固定写法
    def close_spider(self,spider):
        self.f.close()
        print('爬取结束')
        spider.crawler.engine.close_spider(spider,'done')

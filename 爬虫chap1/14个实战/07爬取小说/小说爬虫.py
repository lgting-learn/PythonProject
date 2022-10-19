'''
爬取小说(https://www.quanben.net/4/4408/)
---涉及知识点：
网页解析方式一：
from bs4 import BeautifulSoup
1、BeautifulSoup(response,'lxml')，response必须是request.get().text,不可以是content
2、BeautifulSoup解析html bs4对象可使用 select()/select_one()，类似css的方式获取标签内容或是属性值
   使用 select()/select_one() 时，标签名不加任何修饰，类名前加点，id名前加 #，属性用 [属性=’xxxx’]。
   select() 返回类型是 list。
   select_one() 返回值是list的首个。
   get_text() 获取标签的值文本值：(1) select()[0].get_text() (2) select_one().get_text()
网页解析方式二：
from lxml import etree
#tree.HTML()构造xpath解析对象
.xpath('//div[@class="xx"]//a//@href')
.xpath('//div[@class="xx"]//span//text()')
'''
import requests
from bs4 import BeautifulSoup
import time
import random


def down(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)',
    }
    response = requests.get(url, headers=headers)
    html = response.text
    return html


if __name__ == '__main__':
    url = 'https://www.quanben.net/4/4408/'
    html = down(url)
    # print(html)
    # 创建bs对象 bs是使用的python默认的解析器，lxml也是解析器
    soup = BeautifulSoup(html, 'lxml')
    # 写 CSS 时，标签名不加任何修饰，类名前加点，id名前加 #，在这里我们也可以利用类似的方法来筛选元素，用到的方法是 soup.select()，返回类型是 list
    # >选择器 chapterlist的儿子节点
    ls = soup.select('.chapterlist > dd')
    # 去掉列表中前十个元素，对后面的元素进行操作
    ls = ls[10:]
    print('len:', len(ls))
    for item in ls:
        # 获取属性值
        # 使用 select()/select_one() 时，标签名不加任何修饰，类名前加点，id名前加 #，属性用 [属性=’xxxx’]。
        # select() 返回类型是 list。
        # select_one() 返回值是list的首个。
        detail_url = 'https://www.quanben.net' + item.select_one('a')['href']
        # print('detail_url:',detail_url)
        detail_html = down(detail_url)
        soup_detail = BeautifulSoup(detail_html, 'lxml')
        #get_text()获取标签的值
        title = soup_detail.select_one('#BookCon > h1').get_text()
        print('title:', title)
        content = soup_detail.select_one('#BookText').get_text()
        print('content:', content)
        print('=' * 600)
        time.sleep(random.random() * 2)

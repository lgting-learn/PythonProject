

'''
---涉及知识点：
1、爬取链家二手房（https://sh.lianjia.com/ershoufang/rs/）：提取标题，链接，单价，总价，基本信息，房源特色信息
2、etree.HTML()构造xpath解析对象
3、获取内容易错点：
（1）//与/的使用 获取子元素最好用/
（2）text()获取标签内容
（3）bases[0].xpath('./text()') ./表示在bases[0]下继续截取标签
4、数据写入到mysql:
import pymysql
    #链接数据库
    #主机地址 端口号 用户名 密码 数据库名
    conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='115336',db='lianjia')
    cur = conn.cursor()

    #清空表数据
    sqlstr = 'truncate table lianjia_table'
    #插入语句
    sqlstr = 'insert into lianjia_table(title,link,price,item_base) values (%s,%s,%s,%s)'
    #执行语句
    params=[title,link,price,item_base]
            cur.execute(sqlstr,params)
    #commit之后， 数据库的数据才会改变
    conn.commit()

    #关闭数据库连接 !!!在最外层for循环关闭游标
    cursor.close()
    conn.close()
'''

import pymysql as pymysql
import requests
from lxml import etree
import pymysql
import time
import random

def down(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)',
    }
    response = requests.get(url,headers=headers)
    #.text字符串 .content字节码
    html = response.content
    return html

if __name__ =='__main__':
    #链接数据库
    #主机地址 端口号 用户名 密码 数据库名
    conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='115336',db='lianjia')
    cur = conn.cursor()
    for page in range(1,2):
        if page == 1:
            url = 'https://sh.lianjia.com/ershoufang/'
        else:
            url ='https://sh.lianjia.com/ershoufang/pg'+str(page)+'/'
        print('url:'+url)
        #下载页面源码
        html = down(url)
        #构造了一个XPath解析对象并对HTML文本进行自动修正(给代码段前后加上<html><body></html></body>)
        html = etree.HTML(html)
        f=open('./html_test.txt','wb+')
        f.write(requests.get(url=url).content)
        f.close()
        #print(html.decode('utf-8'))
        #!!!F12只有clear LOGCLICKDATA 但下载的源码的实际类名是clear LOGVIEWDATA LOGCLICKDATA
        ls = html.xpath('//li[@class="clear LOGVIEWDATA LOGCLICKDATA"]//div[@class="title"]/a')
        print('len:',len(ls))
        for each in ls:
            link = each.xpath('./@href')[0]
            print('link:',link)
            detail_html = down(link)
            detail_html = etree.HTML(detail_html)
            #直接在需要查找内容的标签后面加一个/text()
            title = detail_html.xpath('//h1[@class="main"]/text()')[0]
            print('title:',title)
            total_price = detail_html.xpath('//div[@class="price "]/span[@class="total"]/text()')[0]
            print('total_price',total_price)
            total_unit = detail_html.xpath('//div[@class="price "]/span[@class="unit"]//text()')[0]
            print('total unit:',total_unit)
            price = detail_html.xpath('//span[@class="unitPriceValue"]/text()')[0]
            print('price:',price)
            unit = detail_html.xpath('//span[@class="unitPriceValue"]/i/text()')[0]
            print('unit:',unit)
            community_name = detail_html.xpath('//div[@class="communityName"]/a[@class="info "]/text()')[0]
            print('community name:',community_name)
            area = detail_html.xpath('//div[@class="areaName"]/span[@class="info"]//text()')
            area = ''.join(area)
            print('area:',area)
            #!!!/div[@class="content"]
            bases = detail_html.xpath('//div[@class="base"]/div[@class="content"]//li')
            item_base=''
            for base_item in bases:
                label = base_item.xpath('./span[@class="label"]//text()')[0]
                content = base_item.xpath('./text()')[0]
                one_base = label + ':' + content+' '
                item_base+=one_base
            # print('item_base==',item_base)
            sqlstr = 'insert into lianjia_table(title,link,price,item_base) values (%s,%s,%s,%s)'
            params=[title,link,price,item_base]
            cur.execute(sqlstr,params)
            conn.commit()
        cur.close()
        conn.close()



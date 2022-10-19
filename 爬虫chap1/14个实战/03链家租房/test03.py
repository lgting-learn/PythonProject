
import requests
from lxml import etree
import parsel
import pymysql


# 第二页


# 下载网页源码
def down(url):
    headers = {
        'Cookie': 'lianjia_uuid=d384bd29-6e0b-4651-bd6a-ca533b3c391d; _smt_uid=6032e985.21eeb6b3; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1613949318; UM_distinctid=177c6e0341d66f-0082d7c299390d-73e356b-1fa400-177c6e0341ec39; _jzqc=1; _qzjc=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22177c6e03667964-0acefb9a2d4ab4-73e356b-2073600-177c6e036689dd%22%2C%22%24device_id%22%3A%22177c6e03667964-0acefb9a2d4ab4-73e356b-2073600-177c6e036689dd%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _ga=GA1.2.1732438155.1613949322; select_city=310000; _jzqckmp=1; _gid=GA1.2.1883507349.1614086559; lianjia_ssid=fe09bc72-b338-97f7-fadd-b9920806ec92; CNZZDATA1253492439=992637239-1613949148-%7C1614112049; CNZZDATA1254525948=1305689952-1613947495-%7C1614114903; CNZZDATA1255633284=541338160-1613947411-%7C1614114814; CNZZDATA1255604082=936606583-1613947795-%7C1614115210; _jzqa=1.1358683607484987600.1613949319.1614091023.1614117239.5; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiMTc0MjZlY2U2ZGFiNTIwM2Y0ODNkNjM0NWU4YmU1YTU2NTE2YmRiMGMxYWE3MTY0ODA0NjhiM2VmMTRhOGVmZjE1ZjNmYjNlZWNhMTQxM2MwMzFiZWNiYTNhNzEyYjdlOWUyODQ0ODk5NDZiNjg4OTYzZTQ3ZTM0ZTgwMjUyMTU4ODRlMGNlYzNjNWFmNDkxZTI3NDQzZWIxMmU4OGQ4MGQ4ODkxNTJlNDVjODBiNWVlMTBjOWQxYjM2YzZmNjFkZmEwMDc3NjRmMjA1Nzg0MWYwYzY4MmIwYjMwYzlkMmE2NTlmZDdlZjhlZTMyNWU5YmI4ODlhZDhjMjMwYmNlYWY4YjEwOGVkOWU4N2Q5YjgxODY0Y2VmMDJiOWM1NThiNzlhOWFmMTM1NzRiMTU3ZDc2MzkyYWQzODRmOTFlZmFhNGZlN2ZjOTljZGNlMzFjYTVlNGRhZmM5NmI4ZWEwMlwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI2NjZiMjQzY1wifSIsInIiOiJodHRwczovL3NoLmxpYW5qaWEuY29tL2Vyc2hvdWZhbmcvcnMvIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0=; _gat=1; _gat_past=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1614117249; _qzja=1.1034188692.1613949318591.1614091022767.1614117239504.1614117239504.1614117248580.0.0.0.31.5; _qzjb=1.1614117239504.2.0.0.0; _qzjto=2.1.0; _jzqb=1.2.10.1614117239.1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    html_content = requests.get(url=url, headers=headers).content
    xpathObj = etree.HTML(html_content)
    # print('xpathObj==',xpathObj)
    return xpathObj


url = 'https://sh.lianjia.com/ershoufang/pg2/'
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='115336', db='lianjia')
cursor = conn.cursor()
#清空表数据
# sqlstr = 'truncate table lianjia_table'
# #执行语句
# cursor.execute(sqlstr)
# conn.commit()
# #关闭数据库连接 !!!在最外层for循环关闭游标
# cursor.close()
# conn.close()
html = down(url)
urlArr = html.xpath('//li[@class="clear LOGVIEWDATA LOGCLICKDATA"]//div[@class="title"]/a//@href')
# f=open('./html_test.txt','wb+')
# f.write(requests.get(url=url).content)
# f.close()
# print('urlArr==',urlArr)
for href_item in urlArr:
    href_item_html = down(href_item)
    # print('heft_item_html==',heft_item_html)
    # 标题
    item_title = href_item_html.xpath('//h1[@class="main"]//text()')[0]
    price = href_item_html.xpath('//div[@class="price "]/span[@class="total"]//text()')[0]
    # 单位
    unit = href_item_html.xpath('//div[@class="price "]/span[@class="unit"]//text()')[0]
    # 总价
    all_price = price + unit
    # 规模大小
    mainInfo = href_item_html.xpath('//div[@class="room"]/div[@class="mainInfo"]//text()')[0]
    # 基本属性
    baseArr = href_item_html.xpath('//div[@class="base"]/div[@class="content"]//li')
    item_base=''
    for base_item in baseArr:
        label = base_item.xpath('./span[@class="label"]//text()')[0]
        content = base_item.xpath('./text()')[0]
        one_base = label + ':' + content+' '
        item_base+=one_base
    print('item_base==',item_base)
#     sqlstr = 'insert into lianjia_table(title,link,price,item_base) values (%s,%s,%s,%s)'
#     params=[item_title,href_item,all_price,item_base]
#     cursor.execute(sqlstr,params)
#     conn.commit()
# cursor.close()
# conn.close()

        # print('one_base==', one_base)

if __name__ == '__main__':
    pass
    # down()

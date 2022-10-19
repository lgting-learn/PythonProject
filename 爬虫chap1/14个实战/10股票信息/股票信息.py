'''
---涉及知识点：
1、表格-图形化
from pyecharts.charts import Bar安装失败
解决：
使用旧版【官方文档：https://05x-docs.pyecharts.org/#/zh-cn/prepare】
(1) pip install pyecharts==0.1.9.4
(2) from pyecharts import Bar

2、运行完毕浏览器自动打开html文件
os.system("render.html")
'''
#coding=utf-8
from __future__ import unicode_literals
import requests
import json
import os
# from pyecharts.charts import Bar
# from pyecharts import options as opts
from pyecharts  import Bar
cookies = {
    'waptgshowtime': '2020928',
    'qgqp_b_id': 'e2c9bb90d341893a1ea1a1fc34ec3367',
    'st_si': '80853808548968',
    'st_asi': 'delete',
    'cowCookie': 'true',
    'intellpositionL': '1522.39px',
    'intellpositionT': '455px',
    'st_pvi': '27597185955387',
    'st_sp': '2020-09-28^%^2010^%^3A51^%^3A45',
    'st_inirUrl': 'https^%'
                  '^3A^%^2F^%^2Fwww.baidu.com^%^2Flink',
    'st_sn': '49',
    'st_psi': '20200928165714364-113300300813-0765442235',
}

headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'Accept': '*/*',
    'Referer': 'http://data.eastmoney.com/zjlx/detail.html',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

params = (
    ('pn', '1^'),
    ('pz', '50^'),
    ('po', '1^'),
    ('np', '1^'),
    ('ut', 'b2884a393a59ad64002292a3e90d46a5^'),
    ('fltt', '2^'),
    ('invt', '2^'),
    ('fid0', 'f4001^'),
    ('fid', 'f62^'),
    ('fs', 'm:0 t:6 f:^!2,m:0 t:13 f:^!2,m:0 t:80 f:^!2,m:1 t:2 f:^!2,m:1 t:23 f:^!2,m:0 t:7 f:^!2,m:1 t:3 f:^!2^'),
    ('stat', '1^'),
    ('fields', 'f12,f14,f2,f3,f62,f184,f66,f69,f72,f75,f78,f81,f84,f87,f204,f205,f124^'),
    ('rt', '53376118^'),
    # ('cb', 'jQuery1830010604800611935472_1601283556806^'),
    ('_', '1601283557045'),
)

response = requests.get('http://push2.eastmoney.com/api/qt/clist/get', headers=headers, params=params, cookies=cookies)

# print(response.text)

resp_dict = json.loads(response.text)
# print(resp_dict)

datas = resp_dict.get('data').get('diff')
print(datas)

compiles = []
prices = []

for data in datas:
    print(data)
    # 1.公司名
    company = data.get('f14')

    share_one = data.get('f184')
    share_five = data.get('f165')
    share_ten = data.get('f175')
    # 2.当天股价
    price = data.get('f2')

    # if share_one >= 10 and share_five >= 10 and share_ten >= 5:
    compiles.append(company)
    prices.append(price)
print(compiles)
print(prices)

# 数据可视化

bar = Bar()
# bar.add_xaxis(compiles)
bar.add('股价图',prices)
bar.render('股价图.html')
os.system('股价图.html')

























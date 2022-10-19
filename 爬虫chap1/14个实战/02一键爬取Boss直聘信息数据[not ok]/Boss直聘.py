from selenium import webdriver
from bs4 import BeautifulSoup
import time,random
import requests
# 无头浏览器开启
# driver = webdriver.Chrome(r'C:\Users\86183\AppData\Local\Temp\2.46\chromedriver\chromedriver.exe')

# 城市json
citys = [{"name": "北京", "code": 101010100, "url": "/beijing/"}, {"name": "上海", "code": 101020100, "url": "/shanghai/"},
         {"name": "广州", "code": 101280100, "url": "/guangzhou/"}]

# 每个城市爬取
for city in citys:

    # 只获取前十页
    urls = ['https://www.zhipin.com/c{}/?query=python&page={}&ka=page-{}'.format(city['code'], i, i) for i in
            range(1, 5)]

    for url in urls:
        # time.sleep(random.random*10)
        #requests.get(url)
        response=requests.get(url)

        # 获取源码，解析
        # html = driver.page_source
        html = driver.page_source
        bs = BeautifulSoup(html, 'html.parser')

        job_all = bs.find_all('div', {"class": "job-primary"})
        # print(job_all)

        for job in job_all:
            time.sleep(1)
            # 工作名称
            job_name = job.find('span', {"class": "job-name"}).get_text()
            # 工作地点
            job_place = job.find('span', {'class': "job-area"}).get_text()
            # 工作公司
            job_company = job.find('div', {'class': 'company-text'}).find('h3', {'class': "name"}).get_text()
            # 工作薪资
            job_salary = job.find('span', {'class': 'red'}).get_text()
            # 工作学历
            job_education = job.find('div', {'class': 'job-limit'}).find('p').get_text()[-2:]
            # 工作标签
            job_label = job.find('a', {'class': 'false-link'}).get_text()

            # 注：csv编码需更改为utf-8(若编码不为UTF-8）另：下载后需用记事本打开再另存为时将编码改为带BOM的UTF-8格式
            with open('job.csv', 'a+', encoding='UTF-8-SIG') as fh:
                # 处理避免读取歧义
                fh.write(job_name.replace(',',
                                          '、') + "," + job_place + "," + job_company + "," + job_salary + "," + job_education + ',' + job_label + "\n")

                # 检验成功写入、并成功获取数据
                print(
                    '工作:' + job_name + "，地区:" + job_place + ",公司:" + job_company + ",薪资:" + job_salary + ',学历:' + job_education + ",标签:" + job_label,
                    end="\n")

# 关闭无头浏览器，减少内存损耗
# driver.quit()
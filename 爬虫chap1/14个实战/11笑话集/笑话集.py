'''
爬取笑话集()
---涉及知识点：
1、
'''
import requests
import re
import time
import random

def down(url):
    head = {}
    #写入User Agent信息
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    response = requests.get(url,headers=head)
    html = response.content.decode(response.apparent_encoding,'ignore')
    return html

if __name__ == '__main__':
    # 提取笑话条目
    pat_item = re.compile(r'table.*?width="646".*?>(.*?)</table>', re.M | re.S)
    # 笑话标题
    pat_title = re.compile(r'<td.*?width="408".*?<a.*?>(.*?)</a>', re.M | re.S)
    # 笑话的链接
    pat_url = re.compile(r'<td.*?width="408".*?href="(.*?)"', re.M | re.S)
    # 浏览次数
    pat_nums = re.compile(r'<td.*?width="124".*?>(.*?)</td>', re.M | re.S)
    # 发布时间
    pat_date = re.compile(r'<span.*?class="date">(.*?)</span>', re.M | re.S)
    # 笑话内容
    pat_content = re.compile(r'(<span id="text110">.*?</span>)', re.M | re.S)


    for page in range(1,2):
        if page == 1:
            url = 'http://www.jokeji.cn/hot.htm'
        else:
            url = 'http://www.jokeji.cn/hot.asp?me_page='+str(page)
        html = down(url)
        #print(html)
        ls = pat_item.findall(html)
        print('len:',len(ls))
        for each in ls:
            # 标题
            match_obj = pat_title.search(each)
            if match_obj != None:
                title = match_obj.group(1)
            else:
                title = '空'
            print('title:',title)
            #链接
            match_obj = pat_url.search(each)
            if match_obj != None:
                link = 'http://www.jokeji.cn'+match_obj.group(1)
            else:
                link = '空'
            print('link:', link)
            # 浏览次数
            match_obj = pat_nums.search(each)
            if match_obj != None:
                nums = match_obj.group(1)
            else:
                nums = '空'
            print('nums:', nums)
            # 发布时间
            match_obj = pat_date.search(each)
            if match_obj != None:
                pub_date = match_obj.group(1)
                pub_date = pub_date.strip()
            else:
                pub_date = '空'
            print('pub_date:', pub_date)

            # 笑话内容
            detail_html = down(link)
            #print(detail_html)
            match_obj = pat_content.search(detail_html)
            if match_obj != None:
                content = match_obj.group(1)
            else:
                content = '空'
            print('content:', content)
            print('='*200)

            result = "title:"+title+",link:"+link+',nums:'+nums +',pub_date:'+pub_date +',content:'+content + r'\n'
            with open('./xhj.txt','a',encoding='utf-8') as file:
                file.write(result)
            time.sleep(random.random())
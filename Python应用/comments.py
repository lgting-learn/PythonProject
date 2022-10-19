import requests
import json
import time
import json
import pymysql
from threading import Thread, Lock



def work(user_name, head_img, rate, appraise_time, appraise_detail, appraise_img, restaurant_id):
    print('1111===', user_name, head_img, rate, appraise_time, appraise_detail, appraise_img, restaurant_id)
    # lock.acquire()  # 锁住
    sqlstr = 'insert into user_appraise_python(user_name,head_img,rate,appraise_time,appraise_detail,appraise_img,restaurant_id) values (%s,%s,%s,%s,%s,%s,%s)'
    params = [user_name, head_img, rate, appraise_time, appraise_detail, appraise_img, restaurant_id]
    # 执行语句
    cursor.execute(sqlstr, params)
    # commit之后， 数据库的数据才会改变
    conn.commit()
    # lock.release()  # 解锁


if __name__ == "__main__":
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='115336', db='elemensys')
    # 创建游标
    cursor = conn.cursor()
    sqlstr = 'select * from shop limit 1000'
    # 执行语句
    cursor.execute(sqlstr)
    #读取所有数据
    data = cursor.fetchall()
    addRestaurantId = []
    for item in data:
        addRestaurantId.append(item[0])
    # print('addRestaurantId===', addRestaurantId)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
        'Cookie': '_lxsdk_cuid=1768aab94844e-0fcb5d4e4509fc-c791039-1fa400-1768aab9485c8; uuid=65c034db444945ddb34f.1614725864.1.0.0; __mta=19111303.1614725864762.1614725864762.1614725864762.1; ci=91; rvct=91; userTicket=lphnwqxKehfXboMabfJpRcWWnNJZUrMdqgXydgbk; lsu=; _hc.v=6bd62f1a-3a2f-0460-da68-3a8d90b66c6a.1614726302; IJSESSIONID=node0166j0r3uytl058x20sxek9jl17965975; iuuid=FE72403B6F05D7D0B668997C9562BB4ED0C4622258B8192CC4961B3D09A69FF9; cityname=%E4%B8%9C%E8%8E%9E; _lxsdk=FE72403B6F05D7D0B668997C9562BB4ED0C4622258B8192CC4961B3D09A69FF9; p_token=LC17HT797QRyPnIninDHaz4G_XMAAAAA5gwAANXR-jEQV9vrJRr7YwQ9we6QxCcZhMR73Mmz3b27ciuA42rkDbAvNWZRHayyrGpdBg; webp=1; __utmc=74597006; __utmz=74597006.1614812307.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ci3=1; meishi_ci=91; cityid=91; wm_order_channel=mtib; utm_source=60030; request_source=openh5; au_trace_key_net=default; openh5_uuid=FE72403B6F05D7D0B668997C9562BB4ED0C4622258B8192CC4961B3D09A69FF9; __utma=74597006.231339156.1614812307.1615088621.1615186133.3; latlng=22.954358,113.911575,1615186133188; i_extend=C_b1Gimthomepagecategory1394H__a; client-id=4e06bf80-bf15-4109-9666-cfce1907d11c; cssVersion=3a77c630; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; mtcdn=K; lat=23.01391; lng=114.08768; token2=zzTMtWpPAuCXs0Ua57Y1XZxsleEFAAAABg0AAJrRxdwk4aejgtsOhBXxa0JLF7EaQqu91nl7oo13XAbYdY74sdgJM8f6ogb9o54Dpg; lt=zzTMtWpPAuCXs0Ua57Y1XZxsleEFAAAABg0AAJrRxdwk4aejgtsOhBXxa0JLF7EaQqu91nl7oo13XAbYdY74sdgJM8f6ogb9o54Dpg; u=643203934; n=ptx544075544; unc=ptx544075544; firstTime=1615601720975; _lxsdk_s=1782950fbf4-afe-a95-64a%7C%7C19'
    }
    lock = Lock()
    # 每次获取每家店铺10条评论
    page = 10
    for i in range(0, 160):
        try:
            url = "https://www.meituan.com/meishi/api/poi/getMerchantComment?uuid=65c034db444945ddb34f.1614725864.1.0.0&platform=1&partner=126&originUrl=https%3A%2F%2Fwww.meituan.com%2Fmeishi%2F5233663%2F&riskLevel=1&optimusCode=10&id=5233663&userId=643203934&offset={}&pageSize={}&sortType=1".format(
                i * page, page)
            print('外层url', url)

            resp = requests.get(url=url, headers=headers).json()
            print('外层try', resp)

            comments = resp['data']['comments']
            l = []
            for j in comments:
                # print('resp0310 comments===', j)
                user_name = j['userName']
                head_img = j['userUrl']
                rate = int(j['star'] / 10)
                appraise_time = j['commentTime']
                appraise_detail = j['comment']
                if len(j['picUrls']) > 0:
                    # 数组转json，直接存数据报错:expected str instance, dict found
                    appraise_img = json.dumps(j['picUrls'])

                else:
                    appraise_img = ''
                restaurant_id = addRestaurantId[i]
                try:
                    work(user_name, head_img, rate, appraise_time, appraise_detail, appraise_img, restaurant_id)
                    # p = Thread(
                    #     target=work(user_name, head_img, rate, appraise_time, appraise_detail, appraise_img, restaurant_id))
                except Exception as e:
                    continue
                    print('异常===', e)
                    print('异常===', user_name, head_img, rate, appraise_time, appraise_detail, type(appraise_img),
                          restaurant_id)
                # --------写入user_appraise表

                # l.append(p)
                # p.start()
                # for p in l:
                #     p.join()
        except Exception as e:
            continue
            print('外层for循环异常：', e)
            # print('外层for循环异常：',resp)

    # 关闭数据库连接 !!!在最外层for循环关闭游标
    cursor.close()
    conn.close()
    print('写入完成')

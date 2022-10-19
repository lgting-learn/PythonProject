import requests
import pymysql
import time

# 美团爬取数据经验：
# 1、非详情页数据一般可以获取
# 2、PC端数据爬取不到，可以考虑移动端/App/小程序

# ques:
# 1、cookie生成
# 获取移动端一级链接  startIndex-第几页
for startIndex in range(1,10):
    url = 'https://i.waimai.meituan.com/openh5/homepage/poilist?startIndex={}&sortId=0&geoType=2&uuid=FE72403B6F05D7D0B668997C9562BB4ED0C4622258B8192CC4961B3D09A69FF9&platform=3&partner=4&originUrl=https://h5.waimai.meituan.com/waimai/mindex/home?type=main_page%26utm_source=60030%26channel=mtib%26stid_b=1%26cevent=imt%2Fhomepage%2Fcategory1%2F394%26region_id=1000450200%26region_version=1614814181882%26isSetRouterProxyRequest=true&riskLevel=71&optimusCode=10&firstcategoryid=0&wm_latitude=0&wm_longitude=0&wm_actual_latitude=22952017&wm_actual_longitude=113939266&openh5_uuid=FE72403B6F05D7D0B668997C9562BB4ED0C4622258B8192CC4961B3D09A69FF9&_token=eJxVUGuvojgA/S8k4xeMUEHAm5CN+EIQARVQJpMbKBWQNxQUNvvfl5ud2ckkTc6jp0nP+ZuoDwHxAWjA02BKdKgmPggwo2ccMSVwM95wgBUAC4S5wLJTAv7hMbywnBJ+bW+Ij+8MR085lv7xZZxH/dv4zebseL4ShzFARBiXzQdFRYvZy4szL55lKMatl89gkVH/WVQW5wF6/4X7Eomjzj9LL0STFmefTdHWEIkcTTP0BEZenqNUzHDsTxocB5++CCYQdSjHYpzhb/NdVGTo6/FIoYdRWNQ9GDmzZCc1CuMi/4wDEdA0zS7oOU3/MsdNmhHF/1sDQZhP4uaC8LloMaqNunj3Z1S1qMEirls0TkeMJbPrWHLE5Cd6PxH/0tq49Zht4jAfGVJ6bNmgyzcrk1qTZ655bE6Z9FIujXpTJN2rrOrikufVu32FGaiOQh503FJJ1SeGC1LQqQbkdcppsRwX0jaT+0VmK2eNlYRW7SOdP3ohB/v1drt42tqlY3WvZ3jfAkvgdKq0OAylJ1fN079fitJ7e45Zo5N2w4nv7VilvwW2NvRBO08OB0C6srrv9/y1clNPfznOQK7v5ZW9r/3no3B3wz2qKaVMIZOyALoV5KUQnoxWk2O/s3T35HBbOLj8eonYhp6HHIDLVZCbS7zr7uYqVTW63Ds+lteDWuRJsoXM3ejLvZSHUiSUd0pT+QcUyFw7GEc7ViHIzJVivOtk+XDL66WoLpAOqZdkKVo9V9e7q1U7GlNlkXblX3JHKW5CvmWBvB3kbvAO1UZqzN09oLc7U7KT29MSSEdxrsWJGczlapNv3V1Y5AbzVhdn29HemqNt9UUUmvKjNIoj6fEG9drsFbiSDR3o52SQrzU21UdC1TXj3UJKeaq2wY/fic9y3rQXy75RTqd0KGaHVCsDGB8ZTreOj6YRMtRZvgk7O12JIvHPv9RvKrI='.format(startIndex)
    print('url==',url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
        'Cookie': '_lxsdk_cuid=1768aab94844e-0fcb5d4e4509fc-c791039-1fa400-1768aab9485c8; uuid=65c034db444945ddb34f.1614725864.1.0.0; ci=91; rvct=91; mtcdn=K; userTicket=lphnwqxKehfXboMabfJpRcWWnNJZUrMdqgXydgbk; lsu=; _hc.v=6bd62f1a-3a2f-0460-da68-3a8d90b66c6a.1614726302; lt=LC17HT797QRyPnIninDHaz4G_XMAAAAA5gwAANXR-jEQV9vrJRr7YwQ9we6QxCcZhMR73Mmz3b27ciuA42rkDbAvNWZRHayyrGpdBg; u=643203934; n=ptx544075544; token2=LC17HT797QRyPnIninDHaz4G_XMAAAAA5gwAANXR-jEQV9vrJRr7YwQ9we6QxCcZhMR73Mmz3b27ciuA42rkDbAvNWZRHayyrGpdBg; unc=ptx544075544; lat=23.004105; lng=113.73039; IJSESSIONID=node0166j0r3uytl058x20sxek9jl17965975; iuuid=FE72403B6F05D7D0B668997C9562BB4ED0C4622258B8192CC4961B3D09A69FF9; isid=1AAA0108558670BFBAD7784BD1B8F820; oops=LC17HT797QRyPnIninDHaz4G_XMAAAAA5gwAANXR-jEQV9vrJRr7YwQ9we6QxCcZhMR73Mmz3b27ciuA42rkDbAvNWZRHayyrGpdBg; mt_c_token=LC17HT797QRyPnIninDHaz4G_XMAAAAA5gwAANXR-jEQV9vrJRr7YwQ9we6QxCcZhMR73Mmz3b27ciuA42rkDbAvNWZRHayyrGpdBg; logintype=normal; cityname=%E4%B8%9C%E8%8E%9E; _lxsdk=FE72403B6F05D7D0B668997C9562BB4ED0C4622258B8192CC4961B3D09A69FF9; p_token=LC17HT797QRyPnIninDHaz4G_XMAAAAA5gwAANXR-jEQV9vrJRr7YwQ9we6QxCcZhMR73Mmz3b27ciuA42rkDbAvNWZRHayyrGpdBg; firstTime=1614812274176; webp=1; __utmc=74597006; __utma=74597006.231339156.1614812307.1614812307.1614812307.1; __utmz=74597006.1614812307.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ci3=1; meishi_ci=91; cityid=91; wm_order_channel=mtib; utm_source=60030; request_source=openh5; au_trace_key_net=default; openh5_uuid=FE72403B6F05D7D0B668997C9562BB4ED0C4622258B8192CC4961B3D09A69FF9; terminal=i; w_utmz="utm_campaign=(direct)&utm_source=5000&utm_medium=(none)&utm_content=(none)&utm_term=(none)"; w_visitid=0718871c-4ac3-451f-b06e-0b9371f695f2; w_token=LC17HT797QRyPnIninDHaz4G_XMAAAAA5gwAANXR-jEQV9vrJRr7YwQ9we6QxCcZhMR73Mmz3b27ciuA42rkDbAvNWZRHayyrGpdBg; openh5_uuid=FE72403B6F05D7D0B668997C9562BB4ED0C4622258B8192CC4961B3D09A69FF9; channelType={%22mtib%22:%220%22}; channelConfig={%22channel%22:%22default%22%2C%22type%22:0%2C%22fixedReservation%22:{%22reservationTimeStatus%22:0%2C%22startReservationTime%22:0%2C%22endReservationTime%22:0}}; w_actual_lat=22952017; w_actual_lng=113939266; w_latlng=22952017,113939266; latlng=22.954922,113.934367,1614814175770; __utmb=74597006.9.9.1614814181318; i_extend=C_b1Gimthomepagecategory1394H__a; cssVersion=e7eeab84; _lx_utm=utm_source%3D60030; _lxsdk_s=177fa2ddeec-3d3-c46-0dd%7C%7C159'
    }

    def getShopList(url):
        resp = requests.post(url, headers=headers).json()
        shopList = resp['data']['shopList']
        write_mysql('elemensys', shopList)
        # return shopList


    # 写入shop、food、shop_food_classify
    def write_mysql(db, list):  # db:数据库名 list:循环数组
        # print('list==', list)
        # conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='115336', db='elemensys')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='115336', db=db)
        # 创建游标
        cursor = conn.cursor()

        ## 清空shop表数据
        # sqlstr = 'truncate table shop'
        # cursor.execute(sqlstr)
        #
        # # 清空shop_food_classify表数据
        # sqlstr = 'truncate table shop_food_classify'
        # cursor.execute(sqlstr)
        #
        # # 清空food表数据
        # sqlstr = 'truncate table food'
        # cursor.execute(sqlstr)

        for index_fir, item in enumerate(list):
            shop_id = item['mtWmPoiId']
            name = item['shopName']
            address = item['address']
            # introduce=item.
            image_path = item['picUrl']
            score = int(item['wmPoiScore']) / 10
            per_capita = item['averagePriceTip']
            month_sales = item['monthSalesTip']

            # # 清空shop表数据
            # sqlstr = 'truncate table shop'
            # cursor.execute(sqlstr)
            #
            # # 清空shop_food_classify表数据
            # sqlstr = 'truncate table shop_food_classify'
            # cursor.execute(sqlstr)
            #
            # # 清空food表数据
            # sqlstr = 'truncate table food'
            # cursor.execute(sqlstr)

            # --------写入shop表
            try:
                # sqlstr = 'insert into shop(id,name,address,image_path,score,per_capita,month_sales) values (%s,%s,%s,%s,%s,%s,%s)'
                # params = [shop_id, name, address, image_path, score, per_capita, month_sales]
                # # 执行语句
                # cursor.execute(sqlstr, params)
                # # commit之后， 数据库的数据才会改变
                # conn.commit()

                # print(shop_id, name, address, image_path, score, per_capita, month_sales)
                url = 'https://i.waimai.meituan.com/openh5/v2/poi/food?geoType=2&wm_poi_id={}&source=shoplist&uuid=FE72403B6F05D7D0B668997C9562BB4ED0C4622258B8192CC4961B3D09A69FF9&platform=3&partner=4&originUrl=https://h5.waimai.meituan.com/waimai/mindex/menu?dpShopId=%26mtShopId=1033731133542801%26utm_source=60030%26channel=mtib%26source=shoplist%26initialLat=22.952017%26initialLng=113.939266%26actualLat=22.952017%26actualLng=113.939266&riskLevel=71&optimusCode=10&wm_latitude=22952017&wm_longitude=113939266&wm_actual_latitude=22952017&wm_actual_longitude=113939266&openh5_uuid=FE72403B6F05D7D0B668997C9562BB4ED0C4622258B8192CC4961B3D09A69FF9&_token=eJxNkVuPokAQhf8LyfoikW6uYkI2XhgB7wI6utkYhBZapUFoFNzsf992N7MzSSd16qtzHqr6F1fYEdeDAGoA8twdFVyPgx3QUTmeoyWbqFDuQlHVJVlTeC78wjQINJmFjsVmxPV+SCrgVRn8fIE16z/BpxJl9l4Omxm4hNK87AlConQeAU4D3EkRplVAOmGWCv+QkGISofo7bXJksJ4c8iBGrYqmhzKrihAZKgASaIVJQAi6GinFx1ZJcXQ4GrAVojsi1MAp/Sa+JVmKXmEmw4CiOCsayLSky60CxTgjBxwZEAAgK0AE4AOym5SsGv8vIeqK2sKli+g6qygqlkVWN2t0q1BJDVpUiJ2OY0um3mtJqGi8JGmMiRoP9VcFEi+J2styeVlYDb5a+ZG9+bDz9mfgL2dm+hGasb9i4xLHhCnkNPRi0mXi9VfJqT3FjZqMmrOfj8zhtetdNLqCt80gsQkw8fUk3H1QzVCxIce7s9hG6T1vCv9YWZHava5DpVi03yNamrEI5oNZ93GTqkl3ss7DcCNP/GiFFc29lZfFSJVrz70vmkmWxtEeOB4utjvLmq6jaoKGTV+MjsFok7nn+WNo62drv997Q0vVPTrLPSBPzvbUDPr4WF7I3bNuWz+ei2DczsF7oI1PT11ZPiPbMZ02WD12D/+cTM1u1vhp0K/SrS6K+lvenAfXsRC4JTzOQH+vrbRbXaPdDtrT/mo1g9ab615xGOdOuSWBGe5HDRoOw0zxCTTbihVSpA8KZR/rrv1UxuGGUIgdczYthrolrDNlSJxB1+vqBNSSUhEs6sm5cO6udXKnSruW53jZeMkzeoendmNllrWptyfBHwinRX3uGwb3+w+amgy0'.format(
                    shop_id)
                # url = 'https://i.waimai.meituan.com/openh5/v2/poi/food?geoType=2&wm_poi_id=1033731133608337&source=shoplist&uuid=FE72403B6F05D7D0B668997C9562BB4ED0C4622258B8192CC4961B3D09A69FF9&platform=3&partner=4&originUrl=https://h5.waimai.meituan.com/waimai/mindex/menu?dpShopId=%26mtShopId=1033731133542801%26utm_source=60030%26channel=mtib%26source=shoplist%26initialLat=22.952017%26initialLng=113.939266%26actualLat=22.952017%26actualLng=113.939266&riskLevel=71&optimusCode=10&wm_latitude=22952017&wm_longitude=113939266&wm_actual_latitude=22952017&wm_actual_longitude=113939266&openh5_uuid=FE72403B6F05D7D0B668997C9562BB4ED0C4622258B8192CC4961B3D09A69FF9&_token=eJxNkVuPokAQhf8LyfoikW6uYkI2XhgB7wI6utkYhBZapUFoFNzsf992N7MzSSd16qtzHqr6F1fYEdeDAGoA8twdFVyPgx3QUTmeoyWbqFDuQlHVJVlTeC78wjQINJmFjsVmxPV+SCrgVRn8fIE16z/BpxJl9l4Omxm4hNK87AlConQeAU4D3EkRplVAOmGWCv+QkGISofo7bXJksJ4c8iBGrYqmhzKrihAZKgASaIVJQAi6GinFx1ZJcXQ4GrAVojsi1MAp/Sa+JVmKXmEmw4CiOCsayLSky60CxTgjBxwZEAAgK0AE4AOym5SsGv8vIeqK2sKli+g6qygqlkVWN2t0q1BJDVpUiJ2OY0um3mtJqGi8JGmMiRoP9VcFEi+J2styeVlYDb5a+ZG9+bDz9mfgL2dm+hGasb9i4xLHhCnkNPRi0mXi9VfJqT3FjZqMmrOfj8zhtetdNLqCt80gsQkw8fUk3H1QzVCxIce7s9hG6T1vCv9YWZHava5DpVi03yNamrEI5oNZ93GTqkl3ss7DcCNP/GiFFc29lZfFSJVrz70vmkmWxtEeOB4utjvLmq6jaoKGTV+MjsFok7nn+WNo62drv997Q0vVPTrLPSBPzvbUDPr4WF7I3bNuWz+ei2DczsF7oI1PT11ZPiPbMZ02WD12D/+cTM1u1vhp0K/SrS6K+lvenAfXsRC4JTzOQH+vrbRbXaPdDtrT/mo1g9ab615xGOdOuSWBGe5HDRoOw0zxCTTbihVSpA8KZR/rrv1UxuGGUIgdczYthrolrDNlSJxB1+vqBNSSUhEs6sm5cO6udXKnSruW53jZeMkzeoendmNllrWptyfBHwinRX3uGwb3+w+amgy0'

                params = {
                    'geoType': '2',
                    'wm_poi_id': item['mtWmPoiId'],
                    'source': 'shoplist',
                    'uuid': 'FE72403B6F05D7D0B668997C9562BB4ED0C4622258B8192CC4961B3D09A69FF9',
                    'platform': '3',
                    'partner': '4',
                    'originUrl': 'https://h5.waimai.meituan.com/waimai/mindex/menu?dpShopId=&mtShopId={}&utm_source=60030&channel=mtib&source=shoplist&initialLat=22.952017&initialLng=113.939266&actualLat=22.952017&actualLng=113.939266'.format(
                        shop_id),
                    # 'originUrl': 'https://h5.waimai.meituan.com/waimai/mindex/menu?dpShopId=&mtShopId=1033731133608337&utm_source=60030&channel=mtib&source=shoplist&initialLat=22.952017&initialLng=113.939266&actualLat=22.952017&actualLng=113.939266',
                    'riskLevel': '71',
                    'optimusCode': '10',
                    'wm_latitude': '22952017',
                    'wm_longitude': '113939266',
                    'wm_actual_latitude': '22952017',
                    'wm_actual_longitude': '113939266',
                    'openh5_uuid': 'FE72403B6F05D7D0B668997C9562BB4ED0C4622258B8192CC4961B3D09A69FF9',
                    '_token': 'eJxNkVuPokAQhf8LyfoikW6uYkI2XhgB7wI6utkYhBZapUFoFNzsf992N7MzSSd16qtzHqr6F1fYEdeDAGoA8twdFVyPgx3QUTmeoyWbqFDuQlHVJVlTeC78wjQINJmFjsVmxPV+SCrgVRn8fIE16z/BpxJl9l4Omxm4hNK87AlConQeAU4D3EkRplVAOmGWCv+QkGISofo7bXJksJ4c8iBGrYqmhzKrihAZKgASaIVJQAi6GinFx1ZJcXQ4GrAVojsi1MAp/Sa+JVmKXmEmw4CiOCsayLSky60CxTgjBxwZEAAgK0AE4AOym5SsGv8vIeqK2sKli+g6qygqlkVWN2t0q1BJDVpUiJ2OY0um3mtJqGi8JGmMiRoP9VcFEi+J2styeVlYDb5a+ZG9+bDz9mfgL2dm+hGasb9i4xLHhCnkNPRi0mXi9VfJqT3FjZqMmrOfj8zhtetdNLqCt80gsQkw8fUk3H1QzVCxIce7s9hG6T1vCv9YWZHava5DpVi03yNamrEI5oNZ93GTqkl3ss7DcCNP/GiFFc29lZfFSJVrz70vmkmWxtEeOB4utjvLmq6jaoKGTV+MjsFok7nn+WNo62drv997Q0vVPTrLPSBPzvbUDPr4WF7I3bNuWz+ei2DczsF7oI1PT11ZPiPbMZ02WD12D/+cTM1u1vhp0K/SrS6K+lvenAfXsRC4JTzOQH+vrbRbXaPdDtrT/mo1g9ab615xGOdOuSWBGe5HDRoOw0zxCTTbihVSpA8KZR/rrv1UxuGGUIgdczYthrolrDNlSJxB1+vqBNSSUhEs6sm5cO6udXKnSruW53jZeMkzeoendmNllrWptyfBHwinRX3uGwb3+w+amgy0'
                }
                resp_detail = requests.post(url=url, params=params, headers=headers).json()
                # 左侧食品分类 shop_food_classify
                food_spu_tags = resp_detail['data']['food_spu_tags']
                for index_sec, left_item in enumerate(food_spu_tags):
                    # 左侧菜单名称
                    name = left_item['name']
                    # 店铺id
                    restaurant_id = shop_id
                    # 分类食品id自增
                    # category_id = '0305' + str(index_sec)
                    category_id = str(int(time.time())) + str(index_sec)
                    # 图标
                    icon = left_item['icon']
                    try:
                        print('shop_food_classify try==', name, restaurant_id, category_id, icon)

                        # --------写入shop_food_classify表
                        # sqlstr = 'insert into shop_food_classify(name,restaurant_id,id,icon) values (%s,%s,%s,%s)'
                        # params = [name, restaurant_id, category_id, icon]
                        # # 执行语句
                        # cursor.execute(sqlstr, params)
                        # # commit之后， 数据库的数据才会改变
                        # conn.commit()

                        # 左侧菜单对应右边菜式 对应food表
                        spus = left_item['spus']

                        # print('left_item==', name,'\n')
                        for index_third, spus_item in enumerate(spus):
                            try:
                                id = str(spus_item['id']) + str(index_third)
                                name = spus_item['name']
                                introduce = spus_item['description']
                                # score = spus_item[''] #废弃字段
                                image_path = spus_item['picture']
                                # rating_count = spus_item[''] #废弃字段
                                month_sales = spus_item['month_saled']
                                # satisfy_rate = spus_item[''] #废弃字段
                                restaurant_id = shop_id
                                price = spus_item['min_price']
                                category_id = category_id
                                # buy_number = spus_item[''] #废弃字段

                                # --------写入food表
                                # sqlstr = 'insert into food(id,name,introduce,image_path,month_sales,restaurant_id,price,category_id) values (%s,%s,%s,%s,%s,%s,%s,%s)'
                                # params = [id, name, introduce, image_path, month_sales, restaurant_id, price, category_id]
                                # # 执行语句
                                # cursor.execute(sqlstr, params)
                                # # commit之后， 数据库的数据才会改变
                                # conn.commit()

                                # print('spus_item==',
                                #       id,
                                #       name,
                                #       introduce,
                                #       image_path, month_sales,
                                #       restaurant_id,
                                #       price)
                            except Exception as e:
                                print('food表写入异常==', e)
                                continue
                    except Exception as e:
                        print('shop_food_classify表写入异常==', e)
                        continue

            except Exception as e:
                print('shop表写入异常==', e)
                continue
        # 关闭数据库连接 !!!在最外层for循环关闭游标
        cursor.close()
        conn.close()
        print('写入完成')


    # def getUrl(arr):
    #     write_mysql('elemensys',arr)
    #     for item in arr:
    #         mtWmPoiId = item['mtWmPoiId']
    #         print('item==', mtWmPoiId)


    resp = requests.post(url, headers=headers)
    if resp.status_code == 200:
        print('一级链接请求成功')
        getShopList(url)
    else:
        print('请求失败')
    print("resp==", resp)
    # shopList = re


    # f = open('./food_test.txt', 'wb+')
    # f.write(resp)
    # f.close()
    print('ok')

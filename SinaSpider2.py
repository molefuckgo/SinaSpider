# coding:utf-8
import copy

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
import re
# chromedriver = '/Users/edz/Downloads/chromedriver'
# browser = webdriver.Chrome(executable_path=chromedriver)
# # browser.get('https://weibo.com/like/outbox?leftnav=1')
# browser.get('https://weibo.com/3760433950/profile?is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page=3#feedtop')
# wait = WebDriverWait(browser, 60)
# wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="Pl_Official_MyProfileFeed__20"]/div/div[46]/div[1]/div[3]/div[5]/div[2]/div[5]/div[1]/ul/li[3]/span/a/span/em[2]')))
# # print(browser.page_source)
#
# # pattern = re.compile(r'time_sort_comm:(\d+).*?"')
# pattern = re.compile(r'<div minfo="ru=\d+.*?rm=(.*?)"')
# result = pattern.findall(browser.page_source)
# result = list(set(result))
# print(result)
# print(len(result))


# browser.close()
from bs4 import BeautifulSoup
import json

import requests



headers = {'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'SINAGLOBAL=9599935520666.8.1553265404629; _s_tentry=login.sina.com.cn; Apache=3259501995761.24.1553705628236; ULV=1553705628247:2:2:1:3259501995761.24.1553705628236:1553265404645; TC-V5-G0=b993e9b6e353749ed3459e1837a0ae89; Ugrow-G0=e66b2e50a7e7f417f6cc12eec600f517; WBtopGlobal_register_version=4f77457d0350e809; TC-Page-G0=841d8e04c4761f733a87c822f72195f3|1553791034|1553791034; login_sid_t=e39699b2bbed5eba01288506e71a9b22; cross_origin_proto=SSL; YF-V5-G0=8d4d030c65d0ecae1543b50b93b47f0c; UOR=,,login.sina.com.cn; un=18048369219; wvr=6; wb_view_log_7043658711=1440*9002; WBStorage=201903302324|undefined; wb_view_log=1440*9002; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5fnvq4kOrhTVKq2EPAH6_L5JpX5K2hUgL.FoM7ShecSKnNeK22dJLoIEQLxKBLB.BLBK5LxKML1-2L1hBLxKqL1KMLB.2LxKBLB.zL1Kxk1Kz0Sozt; ALF=1585495500; SSOLoginState=1553959501; SCF=AuWczSE6NlqfOAKPgllBwJnt0CgZlcuTcyNGsmv87En6kz9zXiVLHNTtmyrK2Xh-UfOXRSCBTsniFwgAjP_ls4o.; SUB=_2A25xm_oADeRhGeFO71EX9SbLyj2IHXVS0WzIrDV8PUNbmtAKLWvckW9NQX6EvicEL8DqJ7RxSIWjnBJ5ROw6KAif; SUHB=079TjBG3I6UQ1J; YF-Page-G0=70942dbd611eb265972add7bc1c85888|1553959535|1553959509; webim_unReadCount=%7B%22time%22%3A1553959536694%2C%22dm_pub_total%22%3A0%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A15%2C%22msgbox%22%3A0%7D',
            'Host': 'weibo.com',
            'Referer': '',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'}

result = ['3917803641530996', '3828782639148559', '3778936435607793', '3780801134919203',
          '3778937135907330', '4031886294710916', '3994732058958590', '3778932211771756',
          '4032208748226735', '3778937031032275', '3889190690910135', '3781111907653973',
          '3939052669837381', '3917762801527639', '3894257645080425', '3829634212690680',
          '3889193727753034', '3778940994791148', '3876041162072343', '3889220088854522',
          '3876169352650755', '3840555370765451', '3984239093644716', '3778963002172180',
          '3788012481202678', '3828622160380983', '3788546231751806', '4126661416533951',
          '3876558953298317', '3846470354566137', '3778553348507128', '3699616484493803',
          '3701152203916982', '3699619131289704', '3703959564733285', '3743130110689956',
          '3682683470767783', '3701697073365291', '3778408493934907', '3730376247263975',
          '3743046136886070', '3703998491789465', '3684840865863613', '3701107223883749',]

# url = 'https://weibo.com/aj/v6/comment/big?ajwvr=6&id=%s&page=%s' % (i, j)
# print(url)
# page = requests.get(url, headers=headers).text
# page = json.loads(page)
# page = page['data']['html']
# soup = BeautifulSoup(page, 'html.parser')
# divs = soup.find_all("div", class_='WB_text')
# print(len(divs))
# for item in divs:
#     data = str(item.text)
#     print(data.split("："))
# j += 1

import xlwt as xlwt

dataxls = xlwt.Workbook()
sum = 0
table_sum = 1
sum_total = 0
table = dataxls.add_sheet('table%s' % table_sum)
try:
    for i in result:

        j = 1
        while True:
            url = 'https://weibo.com/aj/v6/comment/big?ajwvr=6&id=%s&page=%s' % (i, j)
            print(url)
            pattern = re.compile(r'<div class="empty_con (.*?)"')
            s = requests.get(url, headers=headers).text
            # print(s)
            # print('--s---')
            s = json.loads(s)['data']['html']
            soup = BeautifulSoup(s, 'html.parser')
            divs = soup.find_all("div", class_='WB_text')

            is_empty = re.findall(pattern, s)
            if len(is_empty):
                print('id为', i, '的微博爬取完毕....')
                table.write(sum, 0, 'id为')
                table.write(sum, 1, i)
                table.write(sum, 2, '的微博爬取完毕....')
                sum += 1
                break
            print('-------------------第', j, '页--------------------', '评论个数：', len(divs), '相关微博ID', i)
            table.write(sum, 0, '第%s页，评论个数：%s' % (j, len(divs)))
            # print('sumzai页-------', sum)
            sum += 1
            j += 1
            for item in divs:
                if sum >= 60000:
                    table_sum += 1
                    table = dataxls.add_sheet('table%s' % table_sum)
                    sum_total += sum
                    print('sum_total:', sum_total)
                    sum = 0
                data = str(item.text)
                # print(data.split("：")[0], '---', data.split("：")[1])
                table.write(sum, 0, data.split("：")[0])
                table.write(sum, 1, data.split("：")[1])
                table.write(sum, 2, i)
                sum += 1
            print('table_sum:', table_sum)
            print('sum:', sum)
        # break
except Exception as err:
    print(err)
finally:
    print(sum_total)
    dataxls.save('sinadata2.xls')

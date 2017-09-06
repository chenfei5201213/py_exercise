#-*- coding: utf-8 -*-
# @Time    : 2017/8/23 10:12
# @File    : 星座计算器.py
# @Author  : 守望@天空~
# 根据身份证号码计算出生日期，星座，性别
import datetime

def check(ids):
    # ids = '410102199901242312'
    birth = datetime.date(*map(int,(ids[6:10],ids[10:12],ids[12:14])))
    birthday =  str(birth)
    stars = {"水瓶座": ['01.21', '02.19'],
             "双鱼座": ['02.20', '03.20'],
             "白羊座": ['03.21', '04.20'],
             "金牛座": ['04.21', '05.21'],
             "双子座": ['05.22', '06.21'],
             "巨蟹座": ['06.22', '07.22'],
             "狮子座": ['07.23', '08.22'],
             "处女座": ['08.23', '09.22'],
             "天秤座": ['09.23', '10.23'],
             "天蝎座": ['10.24', '11.22'],
             "射手座": ['11.23', '12.21'],
             "摩羯座": ['12.22', '01.20'],
             }
    for key,value in stars.items():
        start = datetime.date(*map(int,[birth.year]+value[0].split('.')))
        end = datetime.date(*map(int,[birth.year]+value[1].split('.')))
        if (birth.month==12 and birth.day>=22) or (birth.month==1 and birth.day<=20):
            star="摩羯座"
            break
        elif start<=birth<=end:
            star =key
            break

    index  = ids[-4:-1]
    if int(index)%2==0:
        sex= "女"
    else:
        sex= "男"
    print ids
    print birthday,star,sex

# 结合数据生成器，直接生成个人信息数列
from Data_generation.data_generator import data_generator
ggg = data_generator()
for i in range(100):
    id = ggg.id(True)
    print ggg.cname,id['state']
    check(id['id'])
    print ggg.telephone
    print ggg.email
    print
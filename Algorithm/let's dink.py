# -*- coding: utf-8 -*-
# @Time    : 2016/03/19 14:51
# @File    : let's drink.py
# @Author  : 守望@天空~
import sys

print u"题目内容：一瓶酒2元，两个酒瓶换一瓶酒，四个瓶盖换一瓶酒，10元钱可以喝几瓶酒？"

price = 2  #定义啤酒价格
money= 10   #定义本次花费
cw = 2 #定义瓶盖换酒兑换比
bw =4   #定义酒瓶换酒兑换比

if bw==cw or bw<2 or cw<2:
    print u'参数范围不正确'
    print u'cw,bw,不能相等且都应大于2'
    sys.exit(1)
if money/price <min(cw,bw):
    print u'买的也太少了，玩不转啊！'
    sys.exit(1)

print u'啤酒单价%d元/瓶'%price
print u'规则：%d个瓶盖换一瓶酒，%d个酒瓶换一瓶酒' %(bw,cw)
print u'买%d元的酒'%money

sum= 0
wine_n =money/price
caps_n = wine_n
bottle_n = wine_n
sum=sum+wine_n
while bottle_n>=bw or caps_n >=cw:
    print sum ,u'本轮总量+%d ，' %wine_n ,u'瓶盖%d个，瓶子%d个' %(caps_n,bottle_n)
    wine_n=0
    if caps_n>=cw and bottle_n>=bw:
        wine_n =wine_n+ caps_n/cw+bottle_n/bw
        caps_n= caps_n%cw+wine_n
        bottle_n= bottle_n%bw+wine_n
    elif caps_n>=cw and  bottle_n<bw and bottle_n>0:
        wine_n =wine_n+ caps_n/cw
        caps_n= caps_n%cw+wine_n
        bottle_n= bottle_n+wine_n
    elif bottle_n>=bw and caps_n<cw and caps_n>0:
        wine_n =wine_n+ bottle_n/bw
        caps_n= caps_n+wine_n
        bottle_n= bottle_n%bw+wine_n
    else:
         caps_n= caps_n+wine_n
         bottle_n= bottle_n+wine_n
    sum=sum+wine_n
print sum ,u'本轮总量+%d ，' %wine_n ,u'瓶盖%d个，瓶子%d个' %(caps_n,bottle_n)

print
print u'剩余了%d个瓶盖，%d个酒瓶，不换觉得亏了，于是掐指一算'%(caps_n,bottle_n)
a,b=caps_n,bottle_n
borrow= 0
for i in xrange(20):
    if i==((a+i)/cw +(b+i)/bw) and (a+i)%cw==0 and (b+i)%bw==0:
        borrow=i
        break
if  borrow ==0:
    print u'老板：亏本了，不陪你玩了'
    sys.exit(1)

print u'找老板赊了%d瓶啤酒' %borrow

sum=sum+borrow
caps_n=caps_n+borrow
bottle_n=bottle_n+borrow
print sum ,u'本轮总量+%d ，' %borrow ,u'瓶盖%d个，瓶子%d个' %(caps_n,bottle_n)
wine_n= caps_n/cw+bottle_n/bw
caps_n= caps_n%cw
bottle_n= bottle_n%bw
sum = sum+wine_n-borrow
print u'换得%d 瓶酒归还了老板' %wine_n
print sum ,u'本轮总量+%s-%s，' %(wine_n,borrow) ,u'瓶盖%d个，瓶子%d个' %(caps_n,bottle_n)
print u'最终喝到啤酒:%d 瓶' %sum
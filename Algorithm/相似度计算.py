#-*- coding: utf-8 -*-
# @Time    : 2017/8/25 9:29
# @File    : 相似度计算.py
# @Author  : 守望@天空~
# pip install gensim  pyemd
from gensim.models import word2vec
sentences = word2vec.Text8Corpus(u"E:/py_exercise/Algorithm/语料库")
model = word2vec.Word2Vec(sentences, size=200)
# 计算相关度
print model.similarity(u'联系手机',u'联系手机')
print model.similarity(u'申请单位',u'发证时间')
y2 = model.similar_by_word(u'企业', topn=50)  # 20个最相关的
print u"和户籍最相关的词有：\n"
for item in y2:
    print item[0], item[1]
print "--------\n"

a = u"企业注册号,企业名称,住所,经营项目,成立日期,监管日期,监管情况,监管处理意见,企业唯一号".split(',')
b = u"执行人唯一号,企业注册号,企业名称,执行人名称,执行人证件类型,执行人证件号码,企业唯一号".split(',')
c = u"年度,序号,政府投资计划编号,项目名称,建设规模,建设起止年限,总投资,截至上一年底累计完成投资,当年投资计划,当年用地量".split(',')
d = u"年度,序号,项目名称,建设规模,建设起止年限,总投资,截至上一年底累计完成投资,当年投资计划,当年用地量,政府投资计划编号".split(',')
print model.wmdistance(a,b)
print model.wmdistance(a,c)
print model.wmdistance(b,c)
print model.wmdistance(u'国有企事业单位科学技术人员',u'国有企事业单位科学技术人员数')

#-*- coding: utf-8 -*-
# @Time    : 2017/8/21 16:30
# @File    : sqlalchemy_demo2.py
# @Author  : 守望@天空~
# 数据库结构复制，把当前数据库的表结构复制到另一个
from sqlalchemy import create_engine,Table,inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func,MetaData
from sqlalchemy.orm import sessionmaker,relationship,backref
eng = create_engine('mysql+mysqldb://root:admin@localhost/gtester?charset=utf8')
eng2 = create_engine('mysql+mysqldb://root:admin@localhost/sqlalchemy_demo?charset=utf8')
meta = MetaData()
meta.reflect(bind=eng)

for table in meta.sorted_tables:
    # print filter(lambda a: False if a.startswith('_') else True, dir(table))
    print table.description
    table.create(eng2,checkfirst=True)


insp = inspect(eng2)
for table in insp.get_table_names():
    print table, insp.get_columns(table)
    print insp.get_foreign_keys(table)
print insp.get_schema_names()

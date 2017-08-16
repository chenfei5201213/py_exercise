# -*- coding: utf-8 -*-
"""
@Time    : 2017/4/19 9:27
@Author  : 守望@天空~
@File    : config.py
用于日志模块初始化，根据当前路径生成结果输出路径
"""
import logging
import os
import datetime
from logging.handlers import TimedRotatingFileHandler
import sys

project_path = os.path.split(os.path.dirname(__file__))[0]
now = datetime.datetime.now().strftime("%Y-%m-%d_%H%M")
# 指定日志路径
log_path = "%s.log" % now
# 构建logger，指定日志级别
logger = logging.getLogger('logging_demo')
logger.setLevel(logging.INFO)
# 创建文件输出
fh = logging.FileHandler(filename=log_path, encoding='utf-8')
fh.setLevel(logging.INFO)
# 自动清理日志文件
# time_fh = TimedRotatingFileHandler(filename="logs",encoding='utf-8', when="midnight", backupCount=2)
# time_fh.setLevel(logging_demo.INFO)
# 创建命令行输出
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
# 设置日志输出格式
formatter = logging.Formatter(u'%(asctime)s %(filename)s:%(lineno)s %(levelname)s %(message)s')
fh.setFormatter(formatter)
# time_fh.setFormatter(formatter)
ch.setFormatter(formatter)
# 将handler加入到logger
logger.addHandler(fh)
# logger.addHandler(time_fh)
logger.addHandler(ch)
if __name__ =="__main__":
    logger.info(u"u中文？")

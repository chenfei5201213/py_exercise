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

project_path = os.path.split(os.path.dirname(__file__))[0]
now = datetime.datetime.now().strftime("%Y-%m-%d_%H%M")
# 每次测试都创建独立的结果目录
result_path = os.path.abspath(os.path.join(project_path, "result", now))
if not os.path.exists(result_path):
    os.mkdir(result_path)
# 指定日志路径
log_path = os.path.abspath(os.path.join(result_path, "%s.log" % now))
# 构建logger，指定日志级别
logger = logging.getLogger('logging')
logger.setLevel(logging.INFO)
# 　创建文件输出
fh = logging.FileHandler(filename=log_path, encoding='utf-8')
fh.setLevel(logging.INFO)
# 创建命令行输出
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# 设置日志输出格式
formatter = logging.Formatter('%(asctime)s %(filename)s:%(lineno)s %(levelname)s %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# 将handler加入到logger
logger.addHandler(fh)
logger.addHandler(ch)

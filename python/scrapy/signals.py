# -- coding: utf-8 -
"""
@project    :HandBook
@file       :signals.py
@Author     :wooght
@Date       :2024/6/6 17:33
@Content    :scrapy signals
"""
# scrapy 所有信号
# 定义位置:site-packages\scrapy\signals.py
# 引擎开始
engine_started = object()
# 引擎停止
engine_stopped = object()
# 爬虫打开
spider_opened = object()
# 爬虫闲置
spider_idle = object()
# 爬虫关闭
spider_closed = object()
# 爬虫报错
spider_error = object()
# 请求发出/安排
request_scheduled = object()
# 请求被丢弃
request_dropped = object()
# 请求达到下载器
request_reached_downloader = object()
# 请求从下载器出来
request_left_downloader = object()
# 收到响应
response_received = object()
# 响应已经下载
response_downloaded = object()
headers_received = object()
bytes_received = object()
item_scraped = object()
item_dropped = object()
item_error = object()
feed_slot_closed = object()
feed_exporter_closed = object()
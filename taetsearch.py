# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 21:56
# @Author  : ding
# @File    : taetsearch.py

import requests
from lxml import etree
import record
import pandas as pd
from HydroInfoSearch.config import get_config

config = get_config()

proxies = {"https": "https://127.0.0.1:1080", "http": "http://127.0.0.1:1080"}


url1 = 'http://xxfb.mwr.cn/hydroSearch/greatRsvr'
result = requests.post(url1, config['req_header1'])

print(result.status_code)  # 服务器的状态码
print(result.encoding)  # 编码方式
result_text = result.text
result_text_enconde = result_text.encode('utf-8').decode('utf-8')
# 解析HTML网页
html = etree.HTML(result_text_enconde)
table = html.xpath('//tr')
# df = pd.DataFrame(result_text_enconde)
# table = html.xpath('//*[@id="hdtable"]')
# tr = table[0].xpath("./table")
# trr = tr[0].xpath("./tbody")
# trrr = trr[0].xpath("./tr")
pass
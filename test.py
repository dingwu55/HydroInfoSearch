# -*- coding: utf-8 -*-
# @Time    : 2020/6/16 8:35
# @Author  : ding
# @File    : test.py

import requests
from lxml import etree
import urllib.parse

url1 = "http://113.57.190.228:8001/web/report/GetRainReportData/?"
data = {
    'sdate': '2020-06-09 08:00',
    'edate': '2020-06-16 08:00',
}

header = {
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
'Connection': 'keep-alive',
'Content-Type': 'application/json',
'Cookie': 'FSSBBIl1UgzbN7N8001S=mIyOvV6jklSZkriA4rpu67JrbvicHFb0Nd6CUJhsBZXdR6mL0V9YkyLCdGBjPGaP; FSSBBIl1UgzbN7N8001T=40oOVgOnBSwDu9ls32jr5_CgigTtPcg2kYWv0ZZL0tbOiYJHlcbaq_o6JrTj8ZCrZQouooKS1iAHLKOKAAHzZ1C_Wna.NeygTNg051fsKaHhAaJLeJrgKzMqAazVitWKI8_wt4tkz2wNuHLsKoJG.ClFk1adep3e50aRJTWZpgfR8.27oxLbMJgj8NEpZoxmqeZuMHjOyUOQ8Pi0l3_cDRTm20wrMZt_JeSC6oDF1QpS9N5W1LM8gbRD9SqL3sdQAzpxVXuOEdsRC9ZsPZMK4HxdYwB0RzCE52H8nu0szuEo8MXiN2vqVeNit_s76kKuOGQ3n0sYBw27qdfwNfBXM6Xca',
'Host': '113.57.190.228:8001',
'Referer': 'http://113.57.190.228:8001/web/Report/CantonRainSta',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest',
}

DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/77.0.3865.120 Safari/537.36'
}

url = url1 + urllib.parse.urlencode(data)
response = requests.get(url, header)
print(response.encoding)
print(response.status_code)
wb_data = response.text

result_text_enconde = wb_data.encode('utf-8').decode('latin-1')
html = etree.HTML(result_text_enconde)
print('pass')

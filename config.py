# -*- coding: utf-8 -*-
# @Time    : 2020/5/28 16:45
# @Author  : ding
# @File    : config.py


def get_config():
    config = {
        'HOSTNAME': "www.bsimcloud.com",
        'PORT': "7062",
        'DATABASE': "bsimcloud",
        'USERNAME': "bsimcloud",
        'PASSWORD': "BsimCloud_123456",
        'url': 'http://xxfb.mwr.cn/sq_djdh.html',

        'data0': {"callCount": "1",
                  "page=": "/ssIndex.html",
                  "httpSessionId": "457DF20DBA703F85B030FDAEA46034DD.tomcat1",
                  "scriptSessionId": "5481D9BFF3351DC2FF23AE7BBB32F366628",
                  "c0-scriptName": "IndexDwr",
                  "c0-methodName": "getSreachData",
                  "c0-id": "0",
                  "c0-param0": "string:hd",
                  "c0-param1": "string:",
                  "c0-param2": "string:",
                  "batchId": "0"},
        'data1': {"callCount": "1",
                  "page=": "/ssIndex.html",
                  "httpSessionId": "",
                  "scriptSessionId": "16A5D86A2EE55E8BA68DFC78C63DA577996",
                  "c0-scriptName": "IndexDwr",
                  "c0-methodName": "getSreachData",
                  "c0-id": "0",
                  "c0-param0": "string:sk",
                  "c0-param1": "string:",
                  "c0-param2": "string:",
                  "batchId": "1"},
        'data2': {"callCount": "1",
                  "page=": "/ssIndex.html",
                  "httpSessionId": "",
                  "scriptSessionId": "16A5D86A2EE55E8BA68DFC78C63DA577996",
                  "c0-scriptName": "IndexDwr",
                  "c0-methodName": "getSreachData",
                  "c0-id": "0",
                  "c0-param0": "string:yl",
                  "c0-param1": "string:",
                  "c0-param2": "string:",
                  "batchId": "2"},

        'req_header1': {'Accept': 'application/json, text/javascript, */*; q=0.01',
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                        'Connection': 'keep-alive',
                        'Cookie': '__FT10000066=2020-5-26-13-37-40; __NRU10000066=1590471460536; zhuzhan=97700904; JSESSIONID=62EABC4F20C9E5FC4FB8070BC1ACF17A; __REC10000066=4; __RT10000066=2020-6-3-20-55-11',
                        'Host': 'xxfb.mwr.cn',
                        'Referer': 'http://xxfb.mwr.cn/sq_dxsk.html',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
                        'X-Requested-With': 'XMLHttpRequest'

        }

    }
    return config
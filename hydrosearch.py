# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 13:51
# @Author  : ding
# @File    : hydrosearch.py

import requests
from lxml import etree
import record
import pandas as pd
from HydroInfoSearch.config import get_config
config = get_config()

data0 = config["data0"]  # 大江大河
data1 = config["data1"]  # 大型水库
data2 = config["data2"]  # 重点雨水情
require_data = [data0, data1, data2]


def WebSpider(data):
    log = record.log_creater(r'WebSpiderLogging')
    # url1 = 'http://xxfb.mwr.cn/hydroSearch/greatRsvr'
    url1 = 'http://xxfb.mwr.cn/hydroSearch/greatRsvr'
    result = requests.post(config["url"])
    log.info('train r2: %s , train mse: %s ' % (result.status_code, result.encoding))
    print(result.status_code)  # 服务器的状态码
    print(result.encoding)  # 编码方式
    result_text = result.text
    result_text_enconde = result_text.encode('utf-8').decode('utf-8')
    # 解析HTML网页
    html = etree.HTML(result_text_enconde)
    if data["batchId"] == '0':
        table = html.xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tbody/tr')
        table = table[0].xpath('./tr')
        djdh_data = []  # 大江大河数据
        for tr in table:
            liuyu = str(tr.xpath("./td[1]/text()"))
            xingzhenqu = str(tr.xpath("./td[2]/text()"))
            heming = str(tr.xpath("./td[3]/text()"))
            zhanhao = str(tr.xpath("./td[4]/font/@onmouseover")).split(",")[3]
            zhanming = str(tr.xpath("./td[4]/font/@onmouseover")).split(",")[4]
            shijian = str(tr.xpath("./td[5]/text()"))
            shuiwei = str(tr.xpath("./td[6]/font/text()"))
            liuliang = str(tr.xpath("./td[7]/text()"))
            jingjieshuiwei = str(tr.xpath("./td[8]/text()"))
            djdh_data.append(liuyu[2:-2]+","+xingzhenqu[2:-2]+","+heming[2:-2]+","+zhanhao[1:-1]+","+zhanming[1:-4]+","
                            +shijian[2:-2]+","+shuiwei[2:-7]+","+liuliang[2:-2]+","+jingjieshuiwei[2:-14])

        result = [x.split(",") for x in djdh_data]
        if len(result)>3:
            log.info("大江大河数据爬取成功")
        return result

    if data["batchId"] == '1':
        tr = html.xpath("//tr")
        dxsk_data = []  # 大型水库数据
        for tr in tr:
            liuyu = str(tr.xpath("./td[1]/text()"))
            xingzhenqu = str(tr.xpath("./td[2]/text()"))
            heming = str(tr.xpath("./td[3]/text()"))
            zhanhao = str(tr.xpath("./td[4]/font/@onmouseover")).split(",")[0]
            kuming = str(tr.xpath("./td[4]/font/@onmouseover")).split(",")[2]
            shijian = str(tr.xpath("./td[4]/font/@onmouseover")).split(",")[1]
            kushuiwei = str(tr.xpath("./td[5]/font/text()"))
            xushuiliang = str(tr.xpath("./td[6]/text()"))
            rukuliuliang = str(tr.xpath("./td[7]/text()"))
            didinggaocheng = str(tr.xpath("./td[8]/text()"))
            dxsk_data.append(
                liuyu[2:-2] + "," + xingzhenqu[2:-2] + "," + heming[2:-2] + "," + zhanhao[12:-1] + "," + kuming[1:-5]
                + "," + shijian[1:-1] + "," + kushuiwei[2:-6] + "," + xushuiliang[2:-2] + "," + rukuliuliang[2:-2]
                + "," + didinggaocheng[2:-14])

        result = [x.split(",") for x in dxsk_data]
        if len(result)>3:
            log.info("大型水库数据爬取成功")
        return result

    if data["batchId"] == '2':
        tr = html.xpath("//tr")
        zdysq_data = []  # 重点雨水情数据
        for tr in tr:
            liuyu = str(tr.xpath("./td[1]/text()"))
            xingzhenqu = str(tr.xpath("./td[2]/text()"))
            heming = str(tr.xpath("./td[3]/text()"))
            zhanming = str(tr.xpath("./td[4]/text()"))
            shijian = str(tr.xpath("./td[5]/text()"))
            riyuliang = str(tr.xpath("./td[6]/text()"))
            tianqi = str(tr.xpath("./td[7]/text()"))
            zdysq_data.append(
                liuyu[2:-2] + "," + xingzhenqu[2:-2] + "," + heming[2:-2] + "," + zhanming[2:-2] + "," + shijian[2:-2]
                + "," + riyuliang[2:-2] + "," + tianqi[2:-2])
        result = [x.split(",") for x in zdysq_data]
        if len(result) > 3:
            log.info("重点雨水情数据爬取成功")
        return result


if __name__ == '__main__':
    for data in require_data:
        result = WebSpider(data)
        data_pd = pd.DataFrame(result)
        pass

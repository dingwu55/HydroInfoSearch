# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 14:55
# @Author  : ding
# @File    : InfoSearch.py

from selenium import webdriver
import time
import requests
from lxml import etree
url = "http://xxfb.mwr.cn/ssIndex.html?type=2"   # 请求地址
response = requests.post(url=url)
# print(response.encoding)
wb_data = response.text

result_text_enconde = wb_data.encode('utf-8').decode('latin-1')
html = etree.HTML(result_text_enconde)


def col_gain(data_index):
    if data_index == 0:
        table = html.xpath('//*[@id="hdcontent"]/table[3]')
        tr = table[0].xpath("./tr")
        liuyu = str(tr[0].xpath("./td[1]/text()"))
        xingzhenqu = str(tr[0].xpath("./td[2]/text()"))
        heming = str(tr[0].xpath("./td[3]/text()"))
        zhanhao = "站号"
        zhanming = str(tr[0].xpath("./td[4]/text()"))
        shijian = str(tr[0].xpath("./td[5]/text()"))
        shuiwei = str(tr[0].xpath("./td[6]/text()"))
        liuliang = '流量'
        jingjieshuiwei = str(tr[0].xpath("./td[8]/text()"))

        col = [liuyu[2:-2], xingzhenqu[2:-2], heming[2:-2], zhanhao, zhanming[2:-2], shijian[2:-2],
               shuiwei[2:4], liuliang, jingjieshuiwei[2:-2]]
        return col

    elif data_index == 1:
        table = html.xpath('//*[@id="skcontent"]/table[3]')
        tr = table[0].xpath("./tr")
        liuyu = str(tr[0].xpath("./td[1]/text()"))
        xingzhenqu = str(tr[0].xpath("./td[2]/text()"))
        heming = str(tr[0].xpath("./td[3]/text()"))
        zhanhao = '站号'
        kuming = str(tr[0].xpath("./td[4]/text()"))
        shijian = '日期'
        kushuiwei = str(tr[0].xpath("./td[5]/text()"))
        xushuiliang = '蓄水量'
        rukuliuliang = '入库流量'
        didinggaocheng = str(tr[0].xpath("./td[8]/text()"))

        col = [liuyu[2:-2], xingzhenqu[2:-2], heming[2:-2], zhanhao, kuming[2:-2], shijian,
               kushuiwei[2:-2], xushuiliang, rukuliuliang, didinggaocheng[2:-2]]
        return col

    elif data_index == 2:
        table = html.xpath('//*[@id="yscontent"]/table[3]')
        tr = table[0].xpath("./tr")
        liuyu = str(tr[0].xpath("./td[1]/text()"))
        xingzhenqu = str(tr[0].xpath("./td[2]/text()"))
        heming = str(tr[0].xpath("./td[3]/text()"))
        zhanming = str(tr[0].xpath("./td[4]/text()"))
        shijian = str(tr[0].xpath("./td[5]/text()"))
        riyuliang = str(tr[0].xpath("./td[6]/text()"))
        tianqi = str(tr[0].xpath("./td[7]/text()"))
        col = [liuyu[2:-2], xingzhenqu[2:-2], heming[2:-2],
               zhanming[2:-2], shijian[2:-2], riyuliang[2:-2], tianqi[2:-2]]
        return col
    # browser = webdriver.Chrome(r"E:\SimilarDPModel\chromedriver_win32\chromedriver.exe")  # 初始化
# browser.get('http://xxfb.mwr.cn/ssIndex.html?type=2')
# result = browser.find_element_by_xpath('//*[@id="hdcontent"]/table[3]')
# time.sleep(8)
# tr_set = result.find_elements_by_tag_name('tr')
# for tr in tr_set:
#     ss = tr.find_elements_by_tag_name('td')[3].find_elements_by_tag_name('font')
#     ssss = ss.get_attribute('onmouseover')
#
#     print(ss.text)
#
# time.sleep(30)
# with open(r'E:/test1.txt', 'a', encoding='utf-8') as f:
#     text = result.text
#     f.write(text)


if __name__ == '__main__':
    col_list = col_gain(0)

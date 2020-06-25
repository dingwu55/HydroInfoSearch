# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 13:50
# @Author  : ding
# @File    : STCDmapping.py

from HydroInfoSearch import hydrosearch, InfoSearch
from sqlalchemy import create_engine, Column, Table, String, Integer, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
from HydroInfoSearch.config import get_config
config = get_config()

HOSTNAME = config["HOSTNAME"]
PORT = config["PORT"]
DATABASE = config["DATABASE"]
USERNAME = config["USERNAME"]
PASSWORD = config["PASSWORD"]

data0 = config["data0"]  # 大江大河
data1 = config["data1"]  # 大型水库
data2 = config["data2"]  # 重点雨水情
data = [data0, data1, data2]

DB_URI = create_engine("mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8". \
    format(username=USERNAME, password=PASSWORD, host=HOSTNAME, port=PORT, db=DATABASE))
DB_Session = sessionmaker(bind=DB_URI)
session = DB_Session()
# engine = create_engine('oracle://IDBS3:idbs3@www.bsimcloud.com:1726/orcl', echo=True)

csv_data = pd.read_csv(r'E:\SimilarDPModel\data\ST_STBPRP_B.csv', header=1, encoding='ANSI')

result = hydrosearch.WebSpider(data0)
result1 = hydrosearch.WebSpider(data1)
result2 = hydrosearch.WebSpider(data2)
col = InfoSearch.col_gain(0)
col1 = InfoSearch.col_gain(1)
col2 = InfoSearch.col_gain(2)
pd_data = pd.DataFrame(result, columns=col)
pd_data1 = pd.DataFrame(result1, columns=col1)
pd_data2 = pd.DataFrame(result2, columns=col2)

pd_data2["STCD"] = None
for index1 in range(len(pd_data2)):
    for index2 in range(len(csv_data)):
        if pd_data2.iloc[index1, 3] == csv_data.iloc[index2, 1]:
            pd_data2.loc[index1, "STCD"] = csv_data.iloc[index2, 0]
            continue
# pd_data2.to_csv(r'E:/SimilarDPModel/HydroInfoSearch/WebSpiderLogging/pd_data2.csv')
# print(pd_data2)


def w_sql(table_name, data, zd, input_index):
    for i in data.values:
        va = ""
        for j in input_index:
            va += "'" + str(i[j]) + "'" + ", "
        va = va[:-2]
        sql = """INSERT INTO %s (%s) VALUES (%s) """ % (table_name, zd[:-1], va)
        session.execute(sql)
    session.commit()


def to_mysql():
    table_name = 'st_river_r'
    data_pd = pd_data
    zd = "STCD, TM, Z, Q "
    input_index = [3, 5, 6, 7]
    w_sql(table_name, data_pd, zd, input_index)

    table_name1 = 'st_rsvr_r'
    data_pd1 = pd_data1
    zd1 = "STCD, TM, INQ, W, RZ "
    input_index1 = [3, 5, 8, 7, 6]
    w_sql(table_name1, data_pd1, zd1, input_index1)

    table_name2 = 'st_pptn_r'
    data_pd2 = pd_data2
    zd2 = "STNM, WTH, DYP, TM, STCD "
    input_index2 = [3, 6, 5, 4, 7]
    w_sql(table_name2, data_pd2, zd2, input_index2)


if __name__ == '__main__':
    to_mysql()

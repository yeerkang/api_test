# coding:utf-8
import re
from common.config import conf
import requests
import xlrd
import pymysql

from sshtunnel import SSHTunnelForwarder

server = SSHTunnelForwarder(('106.75.222.7', 10422),  # B机器的配置
                            ssh_password='yiguokeji01dev201706',
                            ssh_username='root',
                            remote_bind_address=('10.23.142.249', 3306))  # A机器的配置
server.start()
destination_lib = pymysql.connect(host='127.0.0.1',  # 此处必须是127.0.0.1
                                  port=server.local_bind_port,
                                  user='root',
                                  passwd='yiguokeji01db',
                                  db='test')
cur = destination_lib.cursor(cursor=pymysql.cursors.DictCursor)
sw = xlrd.open_workbook('F:\导购信息.xlsx')
table = sw.sheets()[0]
nows = table.nrows
li = []
j = 0
for i in range(0, nows):
    row_data = table.row_values(i)
    if str(row_data[2])[0] == '1' and 'X' not in str(row_data[2]):
        cur.execute('SELECT s.id FROM sales s,store_sales ss WHERE s.id=ss.sales_id AND ss.supplier_id=17359 AND ss.disable=0 AND s.phone = {}'.format(int(row_data[2])))
        salesId = cur.fetchone()
        if salesId:
            cur.execute('update sales set id_card = {} where id = {}'.format(int(row_data[0]), salesId['id']))
            destination_lib.commit()
            li.append(int(row_data[2]))
    j += 1
print(li)
destination_lib.close()

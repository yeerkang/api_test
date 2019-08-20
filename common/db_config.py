import pymysql
from sshtunnel import SSHTunnelForwarder

class DbConfig:
    # 配置数据库连接数据
    def __init__(self,dbname):
        self.server = SSHTunnelForwarder(('123.59.145.148', 22),  # B机器的配置
                                    ssh_password='#Yiguokeji#Dev201807',
                                    ssh_username='qiakr_dev',
                                    remote_bind_address=('10.19.15.90', 3306))  # A机器的配置
        self.server.start()
        self.destination_lib = pymysql.connect(host='127.0.0.1',  # 此处必须是是127.0.0.1
                                          port=self.server.local_bind_port,
                                          user='query',
                                          passwd='yiguokeji01query201807',
                                          db=dbname)
        self.cur = self.destination_lib.cursor(cursor=pymysql.cursors.DictCursor)

    # 获取读取到的第一条数据库数据
    def find_one(self,sql):

        self.cur.execute(sql)
        return self.cur.fetchone()

    # 获取读取到的所有数据库数据
    def find_all(self,sql):

        self.cur.execute(sql)
        return self.cur.fetchall()
    # 关闭数据库连接
    def close_db(self):
        self.server.close()
        self.cur.close()


if __name__ == '__main__':
    a = DbConfig('sms')
    b = a.find_one('select id from sms_template where supplier_id = 16391 ORDER BY id desc')
    print(int(b['id']))
    a.close_db()
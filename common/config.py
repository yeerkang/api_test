"""
自己创建的一个读取配置文件的类
"""

import os
import configparser
from common.contans import CONF_DIR

class ReadConfig(configparser.ConfigParser):

    def __init__(self):
        # 实例化对象
        super().__init__()
        # 加载文件
        #创建加载配置文件的对象
        r = configparser.ConfigParser()
        #读取开关文件
        r.read(os.path.join(CONF_DIR,'env.ini'), encoding='utf-8')
        #判断开关的值，选择加载环境的配置文件
        if r.get('env','switch') == '1':
            self.read(os.path.join(CONF_DIR,'conf_production.ini'), encoding='utf-8')
        else:
            self.read(os.path.join(CONF_DIR, 'conf.ini'), encoding='utf-8')

conf = ReadConfig()


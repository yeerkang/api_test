
"""
创建自己的日志类
"""
import os
import logging
from common.config import conf
from common.contans import LOG_DIR

#配置文件读取
log_name = conf.get("LOG","log_name")
level = conf.get("LOG","log_level").upper()
console_level = conf.get("LOG","console_level").upper()
file_level = conf.get("LOG","file_level").upper()
file_name = conf.get("LOG","log_file")
#拼接日志文件的绝对路径
log_path = os.path.join(LOG_DIR,file_name)

class MyLogging():

    # #第一种方法：
    # def __init__(self,loglevel,logname):
    #     #创建自己的日志收集器
    #     self.my_log = logging.getLogger("my_log")
    #
    #     #设置日志级别
    #     self.my_log.setLevel("DEBUG")
    #
    #     #创建一个日志输出渠道---输出到控制台,并设置输出日志的等级
    #     log_console = logging.StreamHandler()
    #     log_console.setLevel("WARNING")
    #
    #     # 创建一个日志输出渠道---输出到指定的日志文件中,并设置输出日志的等级
    #     log_file = logging.FileHandler(logname,encoding="utf-8")
    #     log_file.setLevel(loglevel)
    #
    #     #将输出渠道添加到日志收集器中
    #     self.my_log.addHandler(log_console)
    #     self.my_log.addHandler(log_file)
    #
    #     #设置日志输出格式
    #     ft = logging.Formatter('%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s')
    #
    #     #设置输出渠道的日志输出的格式
    #     log_console.setFormatter(ft)
    #     log_file.setFormatter(ft)
    #
    #
    # def debug(self,msg):
    #     self.my_log.debug(msg)
    #
    # def info(self,msg):
    #     self.my_log.info(msg)
    #
    # def warning(self,msg):
    #     self.my_log.warning(msg)
    #
    # def error(self,msg):
    #     self.my_log.error(msg)
    #
    # def critical(self,msg):
    #     self.my_log.critical(msg)

    #第二种方法：使用new函数重写
    def __new__(cls, *args, **kwargs):
        #创建自己的日志收集器
        my_log = logging.getLogger(log_name)

        #设置日志级别
        my_log.setLevel(level)

        #创建一个日志输出渠道---输出到控制台,并设置输出日志的等级
        log_console = logging.StreamHandler()
        log_console.setLevel(console_level)

        # 创建一个日志输出渠道---输出到指定的日志文件中,并设置输出日志的等级
        log_file = logging.FileHandler(log_path,encoding="utf-8")
        log_file.setLevel(file_level)

        #将输出渠道添加到日志收集器中
        my_log.addHandler(log_console)
        my_log.addHandler(log_file)

        #设置日志输出格式
        ft = logging.Formatter('%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s')

        #设置输出渠道的日志输出的格式
        log_console.setFormatter(ft)
        log_file.setFormatter(ft)
        return my_log

logger = MyLogging()



# if __name__ == '__main__':
#
#     my_log = MyLogging("DEBUG","log_1.log")
#
#     my_log.debug("_____debug信息_______")
#     my_log.info("_____info信息_______")
#     my_log.warning("_____warning信息_______")
#     my_log.error("_____error信息_______")
#     my_log.critical("_____critical信息_______")




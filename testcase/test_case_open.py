#coding:utf-8
import os
import unittest
import random
import time
from librarys.ddt import ddt,data
from common.read_excel import ReadExcel
from common.logger import logger
from common.config import conf
from common.contans import DATA_DIR
from common.http_request import HttpRequestNoCookie
from common.http_request import HttpRequestCookie
from common.replace import replace
from  common.db_config import DbConfig
from common.replace import ConText

#配置文件读取
file_name = conf.get("EXCEL","excel_path")
read_coloumns = conf.get("EXCEL","read_columns")

@ddt
class TestCaseData(unittest.TestCase):

    #读取excel中的数据
    wb = ReadExcel(os.path.join(DATA_DIR,file_name),"open1")
    cases = wb.read_data_list_obj(read_coloumns)

    @classmethod
    def setUpClass(cls):
        logger.info("开始数据的测试，正在准备")
        """该方法在调用加载该测试用例类的时候会自动执行"""
        #创建request对象
        cls.request = HttpRequestCookie()

    # 登陆测试用例
    @data(*cases)
    def test_customer(self,case):
        # 获取用例在execl中的位置
        self.row = case.case_id + 1

        # 修改url
        if '?' in case.url:
            case.url = conf.get('env','open_url') + case.url + getattr(TestCaseData,'accessToken')
        else:
            case.url = conf.get('env', 'open_url') + case.url

        if '*now*' in case.data:
            case.data = case.data.replace('*now*',str(int(time.time()*10000)))

        if '*phone*' in case.data:
            case.data = case.data.replace('*phone*','152' + str(random.randint(10000000,99999999)))

        # 对存在关键词的内容进行替换
        case.data = replace(case.data)
        # post请求链接中存在?,为data格式。put请求链接中存在?,为json格式

        response = self.request.request(method=case.method, json=eval(case.data), url=case.url)

        # 断言
        if 'accessToken' in str(response.json()):
            setattr(TestCaseData,'accessToken',response.json()['accessToken'])
        logger.info(response.json())
        try:
            # 预期结果：case.expected  实际结果：response.text
            # logger.info("\n预期结果是：{}，\n实际结果是：{}".format(case.expected,response.text))
            if response.json()['code'] == 0 or response.json()['code'] == 20000:
                self.assertEqual(str(case.expected),str(response.json()['code']))
            else:
                self.assertEqual(eval(str(case.expected)), response.json())
        except AssertionError as e:
            # 测试用例不通过
            # logger.error("{}模块的：{}用例不通过，错误是：{}".format(case.module,case.title,e))
            self.wb.write_data(row=case.case_id+1,column=10,msg='failed')
            self.wb.write_data(row=case.case_id+1,column=9,msg=response.text)
            raise e
        else:
            logger.info("{}模块的：{}用例测试通过".format(case.module,case.title))
            self.wb.write_data(row=case.case_id+1,column=10,msg='pass')
            self.wb.write_data(row=case.case_id+1,column=9,msg=response.text)

    @classmethod
    def tearDownClass(cls):
        DbConfig('xmall').close_db()
        DbConfig('sms').close_db()
        logger.info("数据测试用例执行完毕")
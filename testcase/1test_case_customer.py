#coding:utf-8
import os
import unittest
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
import time

#配置文件读取
file_name = conf.get("EXCEL","excel_path")
read_coloumns = conf.get("EXCEL","read_columns")

@ddt
class TestCaseData(unittest.TestCase):

    #读取excel中的数据
    wb = ReadExcel(os.path.join(DATA_DIR,file_name),"customer")
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
        case.url = conf.get('env','url') + case.url

        # 判断是否存在sql语句
        if case.check_sql:
            # 获取sql语句
            key = tuple(eval(case.check_sql).keys())[0]
            # 执行sql语句
            result = DbConfig(key).find_one(eval(case.check_sql)[key])
            # 判断##在url里面，对url进行替换
            if '##' in case.url:
                case.url = str(case.url).replace('##',str(result['id']))
            # 判断是否在参数里面，如果在对参数进行替换
            if '*exchangeaction*' in str(case.data):
                case.data = eval(case.data)
                case.data['exchangeActionIds'] = str(result['id'])
                case.data = str(case.data)
        if '*tag*' in case.data:
            ramdit_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
            case.data = case.data.replace('*tag*',str(ramdit_time))
        # 判断是否存在参数
        # if case.data:
            # 进行替换参数中需要替换的参数

        case.data = replace(case.data)
            # 如果url里面存在？，数据是data类型
        if '?' in case.url:
            if case.method == 'post':
                response = self.request.request(method=case.method, data=eval(case.data), url=case.url)
        # # 没有，数据类型为json类型
            else:
                response = self.request.request(method=case.method, json=eval(case.data), url=case.url)
        else:
            if case.method == 'post':
                response = self.request.request(method=case.method,url=case.url,json=eval(case.data))
            else:
                response = self.request.request(method=case.method, url=case.url, params=eval(case.data))

        # 断言
        try:
            # 预期结果：case.expected  实际结果：response.text
            # logger.info("\n预期结果是：{}，\n实际结果是：{}".format(case.expected,response.text))
            self.assertEqual(str(case.expected),response.json()['status'])
        except AssertionError as e:
            # 测试用例不通过
            # logger.error("{}模块的：{}用例不通过，错误是：{}".format(case.module,case.title,e))
            self.wb.write_data(row=case.case_id+1,column=10,msg='failed')
            self.wb.write_data(row=case.case_id+1,column=9,msg=response.text)
            raise e
        else:
            # print("用例通过")
            logger.info("{}模块的：{}用例测试通过".format(case.module,case.title))
            self.wb.write_data(row=case.case_id+1,column=10,msg='pass')
            self.wb.write_data(row=case.case_id+1,column=9,msg=response.text)

    @classmethod
    def tearDownClass(cls):
        DbConfig('xmall').close_db()
        DbConfig('sms').close_db()
        logger.info("数据测试用例执行完毕")
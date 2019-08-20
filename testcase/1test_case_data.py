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

#配置文件读取
file_name = conf.get("EXCEL","excel_path")
read_coloumns = conf.get("EXCEL","read_columns")

@ddt
class TestCaseData(unittest.TestCase):

    #读取excel中的数据
    wb = ReadExcel(os.path.join(DATA_DIR,file_name),"data")
    cases = wb.read_data_list_obj(read_coloumns)

    @classmethod
    def setUpClass(cls):
        logger.info("开始数据的测试，正在准备")
        """该方法在调用加载该测试用例类的时候会自动执行"""
        #创建request对象
        cls.request = HttpRequestCookie()

    # 登陆测试用例
    @data(*cases)
    def test_login(self,case):
        # 获取用例在execl中的位置
        self.row = case.case_id + 1
        # 修改url
        url = conf.get('env','url') + case.url
        # 判断是否存在参数
        if case.data:
            # 进行替换参数中需要替换的参数
            case.data = replace(case.data)
            # 获取实际结果
            response = self.request.request(method=case.method, params=eval(case.data), url=url, json=eval(case.data))
        else:
            # 获取实际结果
            response = self.request.request(method=case.method,url=url)
        # 断言
        try:
            # 预期结果：case.expected  实际结果：response.text
            logger.info("\n预期结果是：{}，\n实际结果是：{}".format(case.expected,response.text))
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
        logger.info("数据测试用例执行完毕")
from common.config import conf
import os
import unittest
from librarys.HTMLTestRunnerNew  import HTMLTestRunner
from common.contans import CASE_DIR,REPORT_DIR
import time
from common.email_send import send_email

#读取测试报告存放的文件名
file_name = conf.get('report','file_name')
# 获取当前时间
file_name = time.strftime("%Y%m%d%H%M%S",time.localtime()) + file_name

#创建测试集合
suite = unittest.TestSuite()

#加载测试用例
loader = unittest.TestLoader()

#添加测试用例(此处是直接加载目录)
suite.addTest(loader.discover(CASE_DIR))

filepath = os.path.join(REPORT_DIR,file_name)

# 运行测试集合及生成报告
with open(filepath,"wb") as  f:
    runner = HTMLTestRunner(stream=f,
                            verbosity=2,
                            title="自动化测试报告",
                            description="测试用例报告，请查看~",
                            tester="叶二康")
    runner.run(suite)

# 发送测试报告到邮箱

# send_email(filepath)
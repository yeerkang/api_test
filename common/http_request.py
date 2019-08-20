"""
自己封装的发起请求的类
封装的目的：
    1、根据用例中的请求方法，来决定发起什么类型的请求
    2、输出log日志
"""

import requests
from common.logger import MyLogging
import urllib3
from common.read_excel import ReadExcel

#创建loger对象
my_log = MyLogging()
# 去除校验报错
urllib3.disable_warnings()
class HttpRequestNoCookie(object):

    """直接发起不记录cookies信息的请求"""
    def request(self,method,url,params=None,data=None,json=None,headers=None,cookies=None):

        #判断请求方式
        method = method.lower()
        if method == "post":
            if json:
                my_log.info("请求方式是：{}，请求的url地址是：{},参数是：{}".format(method,url,json))
                return requests.post(url=url,json=json,headers=headers,cookies=cookies,verify=False)
            else:
                my_log.info("请求方式是：{}，请求的url地址是：{},参数是：{}".format(method,url,data))
                return requests.post(url=url,data=data,headers=headers,cookies=cookies,verify=False)
        elif method == "get":
            my_log.info("请求方式是：{}，请求的url地址是：{},参数是：{}".format(method,url,params))
            return requests.get(url=url,params=params,headers=headers,cookies=cookies,verify=False)
        elif method == "put":
            if params == None:
                my_log.info("请求方式是：{}，请求的url地址是：{},参数是：{}".format(method, url, params))
                return requests.put(url=url,headers=headers, cookies=cookies, verify=False)
            else:
                my_log.info("请求方式是：{}，请求的url地址是：{},参数是：{}".format(method,url,params))
                return requests.put(url=url,params=params,headers=headers,cookies=cookies,verify=False)

class HttpRequestCookie(object):

    """发起记录cookies信息的请求,给下一次请求用"""

    def __init__(self):
        #创建一个session对象
        self.session = requests.sessions.Session()

    def request(self,method,url,params=None,data=None,json=None,headers=None,cookies=None):

        #判断请求方式
        method = method.lower()
        if method == "post":
            # 判断是否使用json来传参（适用于项目中接口参数有使用json传参的）
            if json:
                my_log.info("请求方式是：{}，请求的url地址是：{},参数是：{}".format(method,url,json))
                return self.session.post(url=url,json=json,headers=headers,cookies=cookies,verify=False)
            else:
                my_log.info("请求方式是：{}，请求的url地址是：{},参数是：{}".format(method,url,data))
                return self.session.post(url=url,data=data,headers=headers,cookies=cookies,verify=False)
        elif method == "get":
            if params:
                my_log.info("请求方式是：{}，请求的url地址是：{},参数是：{}".format(method, url, params))
                return self.session.get(url=url,params=params,headers=headers,cookies=cookies,verify=False)
            else:
                my_log.info("请求方式是：{}，请求的url地址是：{}".format(method,url))
                return self.session.get(url=url, headers=headers, cookies=cookies, verify=False)
        elif method == "put":
            if params:
                my_log.info("请求方式是：{}，请求的url地址是：{},params参数是：{}".format(method, url, params))
                my_log.info(self.session.put(url=url, params=params, headers=headers, cookies=cookies, verify=False))
                return self.session.put(url=url, params=params, headers=headers, cookies=cookies, verify=False)
            elif json:
                my_log.info("请求方式是：{}，请求的url地址是：{},json参数是：{}".format(method, url, json))
                my_log.info(self.session.put(url=url, json=json, headers=headers, cookies=cookies, verify=False))
                return self.session.put(url=url, json=json, headers=headers, cookies=cookies, verify=False)
            else:
                my_log.info("请求方式是：{}，请求的url地址是：{}".format(method, url))
                my_log.info(self.session.put(url=url, headers=headers, cookies=cookies, verify=False))
                return self.session.put(url=url, headers=headers, cookies=cookies, verify=False)
    def close(self):
        self.session.close()






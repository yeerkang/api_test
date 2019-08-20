import re
import time
from common.config import conf
from common.data_time import DataTime

class ConText:
    # 用来储存临时变量
    dstarttime = DataTime().day_start()
    dendtime = DataTime().day_end()
    tstarttime = DataTime().day_start() + 86000000
    tendtime = DataTime().day_end() + 86000000
    wstarttime = DataTime().week_start()
    wendtime = DataTime().week_end()
    mstarttime = DataTime().month_start()
    mendtime = DataTime().month_end()
    ystarttime = DataTime().year_start()
    yendtime = DataTime().year_end()
    exchangeaction = None
    # open-accessToken
    accessToken = None
    orderId = None

# 正则表达式替换
def replace(data):
    # 正则表达式规则
    p = r'#(.+?)#'
    # 循环判断数据中是否存在符合条件的数据
    while re.search(p,data):
        # 获取符合正则表达式的数据内容
        key = re.search(p,data).group(1)
        try:
            # 获取配置文件中需要置换的数据
            value = conf.get('data',key)
        except:
            value = getattr(ConText,key)
        # 将配置文件内容替换掉数据内的数据
        data = re.sub(p,str(value),data,count=1)
    return data




if __name__ == '__main__':
    setattr(ConText,'exchangeaction',1)
    print(getattr(ConText,'exchangeaction'))
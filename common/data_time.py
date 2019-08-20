import time
import datetime
from datetime import timedelta

class DataTime:
    # 获取当天0点的时间戳
    def day_start(self):
        day_start_time = int(time.mktime(time.strptime(time.strftime('%Y-%m-%d 00:00:00'), '%Y-%m-%d %H:%M:%S'))*1000)
        return day_start_time
    # 获取当天24点的时间戳
    def day_end(self):
        day_end_time = int(time.mktime(time.strptime(time.strftime('%Y-%m-%d 23:59:59'), '%Y-%m-%d %H:%M:%S'))*1000)
        return day_end_time
    # 获取本周第一天0点时间戳
    def week_start(self):
        now = datetime.date.today()
        week_start_day = now - timedelta(days=now.weekday())
        week_start_day = int(time.mktime(time.strptime(time.strftime('{} 00:00:00').format(week_start_day), '%Y-%m-%d %H:%M:%S'))*1000)
        return week_start_day
    # 获取本周最后一天24点时间戳
    def week_end(self):
        now = datetime.date.today()
        week_end_day = now + timedelta(days=6 - now.weekday())
        week_end_day = int(time.mktime(time.strptime(time.strftime('{} 23:59:59').format(week_end_day), '%Y-%m-%d %H:%M:%S'))*1000)
        return week_end_day
    # 获取本月第一天0点的时间戳
    def month_start(self):
        month_start_time = int(time.mktime(time.strptime(time.strftime('%Y-%m-01 00:00:00'), '%Y-%m-%d %H:%M:%S'))*1000)
        return month_start_time
    # 获取本月最后一天24点的时间戳
    def month_end(self):
        if datetime.datetime.now().month in [1,3,5,7,8,10,12]:
            month_end_time = int(time.mktime(time.strptime(time.strftime('%Y-%m-31 23:59:59'), '%Y-%m-%d %H:%M:%S'))*1000)
        elif datetime.datetime.now().month in [4,6,9,11]:
            month_end_time = int(time.mktime(time.strptime(time.strftime('%Y-%m-30 23:59:59'), '%Y-%m-%d %H:%M:%S')) * 1000)
        else:
            if datetime.datetime.now().year % 4 == 0:
                month_end_time = time.mktime(time.strptime(time.strftime('%Y-%m-29 23:59:59'), '%Y-%m-%d %H:%M:%S')) * 1000
            else:
                month_end_time = time.mktime(time.strptime(time.strftime('%Y-%m-28 23:59:59'), '%Y-%m-%d %H:%M:%S')) * 1000
        return month_end_time
    # 获取本年第一天0点的时间戳
    def year_start(self):
        year_start_time = int(time.mktime(time.strptime(time.strftime('%Y-01-01 00:00:00'), '%Y-%m-%d %H:%M:%S'))*1000)
        return year_start_time
    # 获取本年最后一天24点的时间戳
    def year_end(self):
        year_end_time = int(time.mktime(time.strptime(time.strftime('%Y-12-31 23:59:59'), '%Y-%m-%d %H:%M:%S'))*1000)
        return year_end_time



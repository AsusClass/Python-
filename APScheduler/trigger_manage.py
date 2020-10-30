# coding=utf-8
# @Time    : 2020/10/30 14:20
# @Author  : Leo
# @Email   : l1512102448@qq.com
# @File    : trigger_manage.py


import pytz
from apscheduler.triggers.interval import IntervalTrigger


TZ = pytz.timezone("Asia/Shanghai")

class TriggerManager(object):
    """
    触发管理器
    """
    def __init__(self):
        pass

    @classmethod
    def interval_trigger(cls, conf):
        """
        间隔触发方法
        :param conf: 配置计划时间
        :return:
        """
        time_args = {"s": 0, "m": 0, "h": 0, "d": 0, "w": 0}

        time_unit = conf['timeUnit']
        time_interval = conf['timeInterval']
        time_args[time_unit] = time_interval

        return IntervalTrigger(seconds=time_args['s'],
                               minutes=time_args['m'],
                               hours=time_args['h'],
                               days=time_args['d'],
                               weeks=time_args['w'],
                               timezone=TZ
                               )

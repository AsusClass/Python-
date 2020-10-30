# coding=utf-8
# @Time    : 2020/10/30 14:03
# @Author  : Leo
# @Email   : l1512102448@qq.com
# @File    : demo.py

from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import  datetime
from trigger_manage import TriggerManager
import time


def tick(**kwargs):
    print('Hi  %s Tick! The time is: %s' % (kwargs['name'], datetime.now()))

if __name__ == '__main__':
    # 定义定时器 指定10个线程运行
    scheduler = BackgroundScheduler(executors={"default": ThreadPoolExecutor(10)})
    # 触发器设置每隔多少时间执行一次  {"timeInterval": 5, "timeUnit": 's'}表示每隔5秒触发一次
    trigger = TriggerManager.interval_trigger(conf={"timeInterval": 5, "timeUnit": 's'})

    # 添加任务：指定执行的函数、触发器、函数的参数、任务的id(唯一标识，方便根据id修改、删除任务)
    scheduler.add_job(tick, trigger,
                      kwargs={
                          "name": "leo"
                      },
                      id="1")
    scheduler.add_job(tick, trigger,
                      kwargs={
                          "name": "bob"
                      },
                      id="2")
    scheduler.start()


    # 根据任务id删除任务
    time.sleep(10)
    scheduler.remove_job(job_id="2")
    #  BackgroundScheduler 运行在Backgroud，但是并不会阻止主程序自己终止，而主程序终止后，BackgroundScheduler 也会终止。
    #  所以要主线程一直执行
    try:
        # 模拟主进程持续运行
        while True:
            time.sleep(10)
            # print('sleep')
    except(KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
        print('Exit The Job!')
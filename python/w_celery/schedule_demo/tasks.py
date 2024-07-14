# -- coding: utf-8 -
"""
@project    :HandBook
@file       :app.py
@Author     :wooght
@Date       :2024/7/2 15:17
@Content    :
"""
from datetime import timedelta
from celery import Celery
from celery.schedules import crontab
import redis
import random
from pytz import timezone


pool = redis.ConnectionPool(host='192.168.101.101', port=6379, db=0, socket_connect_timeout=2)
r = redis.Redis(connection_pool=pool)

task_name_list = ['one', 'two', 'three', 'four', 'five']
print(random.choice(task_name_list))

backend = 'redis://192.168.101.101:6379/0'      # 存储任务结果及状态,将worker的执行结果返回给调用方
broker = 'redis://192.168.101.101:6379/1'       # 存储消息队列,负责接受任务请求,并转发值worker
app = Celery('app',
             broker=broker,
             backend=backend,
             broker_connection_retry_on_startup=True)

app.conf.timezone = 'Asia/Shanghai'
app.conf.enable_utc = False
# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     print('开始定时任务')
#     sender.add_periodic_task(5.0, task_1.s(random.choice(task_name_list)), name='task_1')        # 每隔 5 秒执行
#     sender.add_periodic_task(
#         crontab(hour='17-23', minute='*/10'),
#         task_2.s(random.choice(task_name_list)),
#         name='task_2'
#     )

@app.task
def task_1(name):
    print('task_1 run args:{}'.format(name))
    r.hset('celery_demo', 'one', str(random.randint(1,100)))

@app.task
def task_2(name):
    print('task_2 run args:{}'.format(name))
    r.hset('celery_demo', 'two', str(random.randint(1,100)))

# random 在这里只运行一次 因为只启动一次
app.conf.beat_schedule = {
    'every-ten-seconds':{
        'task': 'tasks.task_1',
        'schedule': timedelta(seconds=10),    # 每隔10秒执行
        'args':(random.choice(task_name_list),),
    },
    'every-one-minutes':{
        'task': 'tasks.task_2',
        'schedule': crontab(minute='*/1'),      # 每分钟执行
        'args':(random.choice(task_name_list),)
    }
}

"""
    启动定时任务分两步:
        1:启动worker  挂载函数等待任务                    celery -A tasks worker -l info
        2:启动beat    周期性提交任务 production 生产任务    celery -A tasks beat -l info
    crontab 参数:
        minute：分钟，取值范围为0-59或者*表示匹配所有分钟。
        hour：小时，取值范围为0-23或者*表示匹配所有小时。
        day_of_week：星期几，取值范围为0-6（0表示周一，6表示周日）或者*表示匹配所有星期几。
        day_of_month：月份中的日期，取值范围为1-31或者*表示匹配所有日期。
        month_of_year：年份中的月份，取值范围为1-12或者*表示匹配所有月份。
        timezone：时区，可以使用pytz.timezone函数来指定时区，默认为None表示使用UTC时区。
        
        schedule = crontab(minute='*/1')                            每分钟
        schedule = crontab(minute=30)                               每小时的第30分钟
        schedule = crontab(minute=0, hour=0)                        每天晚上00:00
        schedule = crontab(minute=0, hour=10, day_of_week=1)        每周一上午10点
        schedule = crontab(minute=0, hour=0, day_of_month=1)        每月1号00:00
        schedule = crontab(minute='*/5', day_of_week='mon,tue')     每周一周二 相隔5分钟执行
        schedule = crontab(minute=0, hour='*/1', day_of_week='mon-fri') 周一到周五 每小时
        schedule = crontab(minute='*/30', hour='9-17')              每天9点到17点 30分钟执行一次
        crontab(hour=22, minute=0, tz=timezone("Asia/Shanghai"))    指定时区
        
    清除积压任务:
        当beat一直执行,而worker未开启时候,会产生很多任务,造成任务积压,当我们开启worker时,会瞬间执行之前的任务
        可以在运行worker时,清楚积压的任务(purge)
        celery -A tasks.app purge       # 根据提示remove所有task

"""
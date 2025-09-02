# 代码生成时间: 2025-09-02 15:29:45
import cherrypy
from cherrypy.process import plugins,服务器
from apscheduler.schedulers.background import BackgroundScheduler
import logging

"""
定时任务调度器服务
"""

# 设置日志
logging.basicConfig(level=logging.INFO)

class SchedulerService:
    def __init__(self):
        # 初始化调度器
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()

    def add_job(self, func, trigger, *args, **kwargs):
        """ 添加定时任务
        
        :param func: 要调度的函数
        :param trigger: 触发器，例如'interval', 'cron'等
        :param args: 函数参数
        :param kwargs: 函数关键字参数
        """
        self.scheduler.add_job(func, trigger, *args, **kwargs)
        logging.info(f'Job added: {func.__name__}')

    def remove_job(self, job_id):
        "
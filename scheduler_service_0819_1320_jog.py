# 代码生成时间: 2025-08-19 13:20:25
import cherrypy
import datetime
from apscheduler.schedulers.background import BackgroundScheduler

class SchedulerService:
    def __init__(self):
        # 初始化调度器
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()

    def add_job(self, func, trigger, **kwargs):
        """添加定时任务
        func: 要执行的函数
        trigger: 触发器类型，如interval, cron等
        kwargs: 触发器相关的参数，如hours, minutes等
        """
        self.scheduler.add_job(func, trigger=trigger, **kwargs)
        cherrypy.log("定时任务添加成功")

    def remove_job(self, job_id):
        """移除定时任务
        job_id: 任务ID
        """
        self.scheduler.remove_job(job_id)
        cherrypy.log("定时任务移除成功")

    def run(self):
        """启动服务"""
        cherrypy.quickstart(self)

    # 示例任务函数
    @cherrypy.expose
    def my_task(self):
        """定时任务示例函数"""
        now = datetime.datetime.now()
        cherrypy.log(f"执行任务：{now}")

# 创建服务实例
scheduler_service = SchedulerService()

# 添加示例定时任务，每5秒执行一次
scheduler_service.add_job(scheduler_service.my_task, 'interval', seconds=5)

# 启动服务
scheduler_service.run()

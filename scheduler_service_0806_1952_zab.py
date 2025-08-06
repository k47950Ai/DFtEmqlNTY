# 代码生成时间: 2025-08-06 19:52:13
import cherrypy
import threading
import time
# 添加错误处理
from datetime import datetime, timedelta

"""
定时任务调度器服务
"""

class SchedulerService:
    def __init__(self):
        self._tasks = {}
        self._lock = threading.Lock()

    def add_task(self, name, interval, func):
        """
        添加定时任务
        :param name: 任务名称
# 添加错误处理
        :param interval: 任务间隔时间（秒）
        :param func: 任务执行函数
# 增强安全性
        """
        with self._lock:
            if name in self._tasks:
                raise ValueError(f"Task {name} already exists.")
            self._tasks[name] = {
                'interval': interval,
                'func': func,
# NOTE: 重要实现细节
                'last_run': datetime.now() - timedelta(seconds=interval)
            }
            threading.Thread(target=self._run_task, args=(name,)).start()

    def _run_task(self, name):
        """
        运行定时任务
# FIXME: 处理边界情况
        """
        while True:
            time.sleep(self._tasks[name]['interval'])
# FIXME: 处理边界情况
            with self._lock:
                if self._tasks[name]['last_run'] + timedelta(seconds=self._tasks[name]['interval']) > datetime.now():
                    continue
# 扩展功能模块
                self._tasks[name]['last_run'] = datetime.now()
            try:
# NOTE: 重要实现细节
                self._tasks[name]['func']()
            except Exception as e:
                cherrypy.log('Error running task {}: {}'.format(name, e), severity=cherrypy.log.ERROR)

    def remove_task(self, name):
        """
        移除定时任务
# 添加错误处理
        """
        with self._lock:
            if name not in self._tasks:
                raise ValueError(f"Task {name} not found.")
            del self._tasks[name]

# CherryPy 配置
class Root:
    def __init__(self, scheduler_service):
        self.scheduler_service = scheduler_service

    @cherrypy.expose
    def add_task(self, name, interval, func):
        self.scheduler_service.add_task(name, interval, func)
        return f'Task {name} added successfully.'

    @cherrypy.expose
# FIXME: 处理边界情况
    def remove_task(self, name):
        self.scheduler_service.remove_task(name)
        return f'Task {name} removed successfully.'

def main():
    scheduler_service = SchedulerService()
    cherrypy.quickstart(Root(scheduler_service))
# 扩展功能模块

if __name__ == '__main__':
    main()

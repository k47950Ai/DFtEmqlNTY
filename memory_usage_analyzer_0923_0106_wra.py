# 代码生成时间: 2025-09-23 01:06:22
import cherrypy
import psutil
import os

# 定义一个类来处理内存使用情况分析
class MemoryUsageAnalyzer:
    def __init__(self):
        # 初始化时，不需要做任何操作
        pass

    # 获取当前进程的内存使用情况
    @cherrypy.expose
    def get_process_memory_usage(self):
        try:
            # 使用psutil获取当前进程的内存使用信息
            process = psutil.Process(os.getpid())
            memory_info = process.memory_info()
            return {"rss": memory_info.rss, "vms": memory_info.vms}
        except Exception as e:
            # 错误处理，返回错误信息
            return {"error": str(e)}

    # 获取系统总内存使用情况
    @cherrypy.expose
    def get_system_memory_usage(self):
        try:
            # 使用psutil获取系统的内存使用信息
            memory = psutil.virtual_memory()
            return {
                "total": memory.total,
                "available": memory.available,
                "used": memory.used,
                "free": memory.free,
                "percent": memory.percent
            }
        except Exception as e:
            # 错误处理，返回错误信息
            return {"error": str(e)}

# 设置CherryPy服务器配置
if __name__ == '__main__':
    conf = {
        '/': {
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'static'
        }
    }

    # 启动CherryPy服务器
    cherrypy.quickstart(MemoryUsageAnalyzer(), config=conf)
# 代码生成时间: 2025-08-30 20:24:14
import cherrypy
import psutil
import json

# 系统性能监控工具
class SystemPerformanceMonitor:
    def __init__(self):
        # 初始化函数
        pass

    # 获取CPU使用率
    @cherrypy.expose
    def get_cpu_usage(self):
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            return json.dumps({'cpu_usage': cpu_usage})
        except Exception as e:
            cherrypy.response.status = 500
            return json.dumps({'error': str(e)})

    # 获取内存使用情况
    @cherrypy.expose
    def get_memory_usage(self):
        try:
            memory = psutil.virtual_memory()
            return json.dumps({'memory_usage': memory.percent})
        except Exception as e:
            cherrypy.response.status = 500
            return json.dumps({'error': str(e)})

    # 获取磁盘使用情况
    @cherrypy.expose
    def get_disk_usage(self):
        try:
            disk_usage = psutil.disk_usage('/')
            return json.dumps({'disk_usage': disk_usage.percent})
        except Exception as e:
            cherrypy.response.status = 500
            return json.dumps({'error': str(e)})

# 设置CherryPy服务器配置
config = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 8080,
    },
    '/': {
        'tools.json_out.on': True,
        'tools.json_out.force': True,
    }
}

# 启动CherryPy服务器
if __name__ == '__main__':
    cherrypy.quickstart(SystemPerformanceMonitor(), config=config)
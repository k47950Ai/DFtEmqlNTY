# 代码生成时间: 2025-09-19 12:08:32
import cherrypy
from subprocess import Popen, PIPE
import psutil
import json

# SystemMonitor 类负责系统性能监控
class SystemMonitor:
    def __init__(self):
        pass

    # 监控CPU使用率
    @cherrypy.expose
    def cpu_usage(self):
        """返回CPU使用率"""
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            return json.dumps({'cpu_usage': cpu_usage})
        except Exception as e:
            return json.dumps({'error': str(e)})

    # 监控内存使用情况
    @cherrypy.expose
    def memory_usage(self):
        """返回内存使用情况"""
        try:
            memory = psutil.virtual_memory()
            memory_usage = memory.percent
            return json.dumps({'memory_usage': memory_usage})
        except Exception as e:
            return json.dumps({'error': str(e)})

    # 监控磁盘使用情况
    @cherrypy.expose
    def disk_usage(self):
        """返回磁盘使用情况"""
        try:
            disk_usage = psutil.disk_usage('/')
            return json.dumps({'disk_usage': disk_usage.percent})
        except Exception as e:
            return json.dumps({'error': str(e)})

    # 监控网络状态
    @cherrypy.expose
    def network_status(self):
        """返回网络状态"""
        try:
            net_io = psutil.net_io_counters()
            return json.dumps({'network_sent': net_io.bytes_sent, 'network_recv': net_io.bytes_recv})
        except Exception as e:
            return json.dumps({'error': str(e)})

# 设置 CherryPy 服务器配置
config = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 9090,  # 设置端口
    }
}

# 启动 CherryPy 服务器
if __name__ == '__main__':
    cherrypy.quickstart(SystemMonitor(), config=config)
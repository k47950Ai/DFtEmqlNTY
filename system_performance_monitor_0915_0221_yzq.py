# 代码生成时间: 2025-09-15 02:21:04
import cherrypy
import psutil
import json
import logging

# 设置日志配置
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SystemPerformanceMonitor:
    """监控系统性能指标的类"""

    @cherrypy.expose
    def monitor(self):
        """提供系统性能监控的接口"""
        try:
            # 收集系统性能数据
            system_data = self.collect_system_data()
            # 将数据格式化为JSON
            return json.dumps(system_data)
        except Exception as e:
            logger.error(f"监控系统性能时发生错误: {e}")
            raise cherrypy.HTTPError(500, "内部服务器错误")

    def collect_system_data(self):
        """收集系统性能数据"""
        system_data = {}
        # 获取CPU使用率
        cpu_usage = psutil.cpu_percent(interval=1)
        system_data['cpu_usage'] = cpu_usage
        # 获取内存使用率
        memory = psutil.virtual_memory()
        system_data['memory_usage'] = memory.percent
        # 获取磁盘使用率
        disk_usage = psutil.disk_usage('/')
        system_data['disk_usage'] = disk_usage.percent
        # 获取网络流量
        net_io = psutil.net_io_counters()
        system_data['network_sent'] = net_io.bytes_sent
        system_data['network_received'] = net_io.bytes_recv
        return system_data

if __name__ == '__main__':
    # 配置CherryPy服务器
    cherrypy.config.update({'server.socket_host': '0.0.0.0',
                            'server.socket_port': 8080})
    # 启动CherryPy服务器
    cherrypy.quickstart(SystemPerformanceMonitor())
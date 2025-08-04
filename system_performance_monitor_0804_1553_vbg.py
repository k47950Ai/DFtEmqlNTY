# 代码生成时间: 2025-08-04 15:53:18
import cherrypy
def get_system_info():
    """
    Fetches system information such as CPU usage, memory usage, etc.
    """
    import psutil
    cpu_usage = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    disk_usage = psutil.disk_usage('/')
    return {
        'cpu_usage': cpu_usage,
        'memory': {'total': memory.total, 'available': memory.available, 'used': memory.used},
        'disk_usage': {'total': disk_usage.total, 'used': disk_usage.used, 'free': disk_usage.free}
    }

def expose_system_info():
    """
    CherryPy endpoint to expose system information.
    """
    try:
        system_info = get_system_info()
        return system_info
    except Exception as e:
        return str(e)

class SystemPerformanceMonitor:
    """
    CherryPy exposed class for system performance monitoring.
    """
    @cherrypy.expose
    def index(self):
        """
        Returns a welcome message and instructions for using the API.
        """
        return "Welcome to the System Performance Monitor API. Use /info to get system information."
    @cherrypy.expose
    def info(self):
        "
# 代码生成时间: 2025-08-11 14:37:16
import os
import cherrypy
def get_system_info():
    """
    Fetches system information such as CPU, memory, and disk usage.
    """
    system_info = {}
    try:
        # CPU Info
        cpu_info = os.popen('top -n 1').readlines()[-3]
        system_info['cpu_usage'] = cpu_info.split()[-2]
        
        # Memory Info
        system_info['mem_usage'] = os.popen('free -m').readlines()[1].split()[3]
        
        # Disk Info
        disk_info = os.popen('df -h /').readlines()[1]
        system_info['disk_usage'] = disk_info.split()[4]
        
        return system_info
    except Exception as e:
        raise cherrypy.HTTPError(500, 'Error fetching system info: ' + str(e))

def get_system_load():
    """
    Fetches system load averages.
    """
    try:
        load_avg = os.getloadavg()
        return {
            '1_min_load': load_avg[0],
            '5_min_load': load_avg[1],
            '15_min_load': load_avg[2]
        }
    except Exception as e:
        raise cherrypy.HTTPError(500, 'Error fetching system load: ' + str(e))

def expose(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return {'error': str(e)}
    wrapper.__doc__ = func.__doc__
    return wrapper

def start_server():
    """
    Starts the CherryPy server.
    """
    class SystemMonitor(object):
        @cherrypy.expose
        @expose
        def info(self):
            """Returns system information."""
            return get_system_info()
        
        @cherrypy.expose
        @expose
        def load(self):
            """Returns system load averages."""
            return get_system_load()
    cherrypy.quickstart(SystemMonitor())
def main():
    """
    Main execution function.
    """
    start_server()
def run_tests():
    """
    Run tests for the system monitor.
    """
    # Test system information
    info = get_system_info()
    print('System Info:', info)
    
    # Test system load
    load = get_system_load()
    print('System Load:', load)
if __name__ == '__main__':
    main()
    # run_tests()  # Uncomment to run tests
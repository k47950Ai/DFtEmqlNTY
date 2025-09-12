# 代码生成时间: 2025-09-12 13:14:22
import cherrypy
import psutil
import subprocess
import json

# 进程管理器类
class ProcessManager:
    """
    该类提供了进程管理的功能，包括启动进程、停止进程和列出当前所有进程。
    """

    @cherrypy.expose
    def index(self):
        """
        返回当前所有进程的列表。
        """
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'status']):
            try:
                processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return json.dumps(processes)

    @cherrypy.expose
    def start_process(self, command):
        """
        启动一个新的进程。
        :param command: 要执行的命令。
        """
        try:
            subprocess.Popen(command, shell=True)
            return json.dumps({'status': 'success', 'message': 'Process started successfully'})
        except Exception as e:
            return json.dumps({'status': 'error', 'message': str(e)})

    @cherrypy.expose
    def stop_process(self, pid):
        """
        停止一个进程。
        :param pid: 要停止的进程的PID。
        """
        try:
            process = psutil.Process(int(pid))
            process.terminate()
            return json.dumps({'status': 'success', 'message': 'Process terminated successfully'})
        except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
            return json.dumps({'status': 'error', 'message': str(e)})

# 设置CherryPy服务器
class HelloWorld(object):
    """
    简单的CherryPy应用，提供根URL的访问。
    """

    @cherrypy.expose
    def index(self):
        return "Hello World!"

# 启动CherryPy服务器
if __name__ == '__main__':
    config = {
        'global': {
            'server.socket_host': '127.0.0.1',
            'server.socket_port': 8080,
        }
    }

    cherrypy.quickstart(HelloWorld(), config=config)
    cherrypy.tree.mount(ProcessManager(), '/processes')

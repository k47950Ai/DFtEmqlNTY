# 代码生成时间: 2025-09-24 10:58:26
import os
import signal
import sys
import threading
from cherrypy import CherryPy, tools
from cherrypy.process import plugins, wsgiserver

# 定义进程管理器类
class ProcessManager:
    def __init__(self):
        # 初始化进程列表
        self.processes = {}

    def start_process(self, pid, command):
        """启动新进程"""
        try:
            # 创建子进程
            process = subprocess.Popen(command, shell=True)
            # 将进程添加到列表中
            self.processes[pid] = process
            return True
        except Exception as e:
            print(f"Error starting process: {e}")
            return False

    def stop_process(self, pid):
        """停止指定PID的进程"""
        if pid in self.processes:
            try:
                # 发送终止信号
                self.processes[pid].send_signal(signal.SIGTERM)
                return True
            except Exception as e:
                print(f"Error stopping process: {e}")
                return False
        else:
            print("Process not found")
            return False

    def list_processes(self):
        """列出所有进程"""
        return list(self.processes.keys())

# 定义CherryPy暴露的接口
class ProcessManagerWebService:
    @cherrypy.expose
    def start(self, pid, command):
        """启动新进程"""
        pm = ProcessManager()
        result = pm.start_process(pid, command)
        return {'result': 'success' if result else 'failure'}

    @cherrypy.expose
    def stop(self, pid):
        """停止指定PID的进程"""
        pm = ProcessManager()
        result = pm.stop_process(pid)
        return {'result': 'success' if result else 'failure'}

    @cherrypy.expose
    def list(self):
        """列出所有进程"""
        pm = ProcessManager()
        return {'processes': pm.list_processes()}

# 配置CherryPy服务器
class CPServer(object):
    def __init__(self):
        self.config = {
            'global': {
                'server.socket_host': '127.0.0.1',
                'server.socket_port': 8080,
                'tools.log_tracebacks.on': True,
            }
        }

    def start(self):
        cherrypy.tree.mount(
            ProcessManagerWebService(),
            '/',
            self.config
        )
        cherrypy.engine.start()
        cherrypy.engine.block()

# 主函数
def main():
    # 创建并启动CherryPy服务器
    server = CPServer()
    server.start()

if __name__ == '__main__':
    main()

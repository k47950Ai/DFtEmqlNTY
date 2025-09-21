# 代码生成时间: 2025-09-21 18:25:56
import cherrypy
def get_all_processes():
    # 使用psutil获取系统中的所有进程信息
    try:
        import psutil
        processes = []
        for process in psutil.process_iter(['pid', 'name', 'status', 'create_time', 'memory_percent']):
            processes.append(process.info)
        return processes
    except ImportError:
        raise cherrypy.HTTPError(500, "Missing required module: psutil")
def kill_process(pid):
    # 杀掉指定pid的进程
    try:
        import psutil
        process = psutil.Process(pid)
        process.terminate()  # 发送SIGTERM信号
        process.wait()  # 等待进程结束
        return {"message": "Process terminated"}
    except psutil.NoSuchProcess:
        raise cherrypy.HTTPError(404, "Process not found")
    except psutil.AccessDenied:
        raise cherrypy.HTTPError(403, "Permission denied")
    except Exception as e:
        raise cherrypy.HTTPError(500, str(e))
def start_process(command):
    # 启动一个新的进程
    try:
        import subprocess
        subprocess.Popen(command, shell=True)
        return {"message": "Process started"}
    except Exception as e:
        raise cherrypy.HTTPError(500, str(e))
def get_process_info(pid):
    # 获取指定pid的进程信息
    try:
        import psutil
        process = psutil.Process(pid)
        return process.info
    except psutil.NoSuchProcess:
        raise cherrypy.HTTPError(404, "Process not found")
    except Exception as e:
        raise cherrypy.HTTPError(500, str(e))
def setup_routes():
    # 设置CherryPy路由
    cherrypy.tree.mount(get_all_processes, "/", {"methods": ["GET"]}, "process_list")
    cherrypy.tree.mount(kill_process, "/kill/{}", {"methods": ["POST"]}, "kill_process")
    cherrypy.tree.mount(start_process, "/start", {"methods": ["POST"]}, "start_process")
    cherrypy.tree.mount(get_process_info, "/info/{}", {"methods": ["GET"]}, "process_info")
def main():
    # 主函数，设置CherryPy配置并启动服务器
    conf = {
        "global": {"server.socket_host": "0.0.0.0",
                  "server.socket_port": 8080},
        "/": {"tools.staticdir.on": True,
               "tools.staticdir.dir": "static"}
    }
    cherrypy.config.update(conf)
    setup_routes()
    cherrypy.quickstart()if __name__ == "__main__":
    main()
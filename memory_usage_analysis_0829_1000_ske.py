# 代码生成时间: 2025-08-29 10:00:38
import cherrypy
def get_memory_usage():
    """获取当前内存使用情况"""
    try:
        import psutil
        mem = psutil.virtual_memory()
        return {"total": mem.total, "available": mem.available, "used": mem.used, "percent": mem.percent}
    except ImportError:
        # 如果没有安装psutil库，返回错误信息
        return {"error": "psutil library is not installed"}

def setup_routes():
    """设置路由，让CherryPy知道如何处理请求"""
    cherrypy.tree.mount(get_memory_usage, "/mem")

def start_server():
    """启动CherryPy服务器"""
    # 设置服务器配置
    cherrypy.config.update({'server.socket_host': '0.0.0.0',
                             'server.socket_port': 8080,
                             'engine.autoreload.on': True})
    # 启动服务器
    setup_routes()
    cherrypy.engine.start()
    cherrypy.engine.block()
def stop_server():
    """停止CherryPy服务器"""
    cherrypy.engine.exit()
    # 清理所有资源
    cherrypy.server.stop()
    # 关闭日志文件等资源
    cherrypy.log.screen_handler.close()
    # 清理全局变量
    cherrypy.tree.close_all()
if __name__ == '__main__':
    # 启动服务器
    start_server()
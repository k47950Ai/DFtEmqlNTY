# 代码生成时间: 2025-09-11 08:37:55
import cherrypy
from cherrypy.lib.static import serve_file
from jinja2 import Environment, FileSystemLoader

# 设置Jinja2模板引擎的配置
TEMPLATES_PATH = 'templates/'
TEMPLATES_ENV = Environment(loader=FileSystemLoader(TEMPLATES_PATH))

# 首页视图函数
class Home:
    exposed = True

    def index(self):
        # 使用Jinja2渲染模板
        template = TEMPLATES_ENV.get_template('index.html')
        return template.render()

    def default(self, *args, **kwargs):
        # 处理404错误
        return self.index()

    def GET(self, *args, **kwargs):
        # 响应GET请求
        return self.default(*args, **kwargs)

    def POST(self, *args, **kwargs):
        # 响应POST请求
        return self.index()

# 静态文件服务
class Static:
    def __init__(self, dir):
        self.dir = dir

    def _cp_dispatch(self, vpath):
        # 服务静态文件
        return serve_file(vpath, dir=self.dir)

    # 响应静态文件请求
    def GET(self, *args, **kwargs):
        return self._cp_dispatch(args[0])

# 配置CherryPy服务器
conf = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 8080,
    },
    '/static': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': 'static',
    },
    '/favicon.ico': {
        'tools.staticfile.on': True,
        'tools.staticfile.filename': 'static/favicon.ico',
    },
}

# 启动CherryPy服务器
if __name__ == '__main__':
    cherrypy.quickstart(Home(), config=conf)

# 代码生成时间: 2025-10-12 22:25:53
import cherrypy
from cherrypy.lib import sessions
from cherrypy.lib.auth import check_password_hash, make_password_hash
import sqlite3
import os

# 配置文件路径
DB_PATH = 'members.db'
SECRET_KEY = 'your_secret_key'

# 数据库初始化函数
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS members
                     (id INTEGER PRIMARY KEY, username TEXT NOT NULL, password_hash TEXT NOT NULL)""")
        conn.commit()

# 会员验证函数
def authenticate(username, password):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT password_hash FROM members WHERE username = ?", (username,))
        password_hash = cursor.fetchone()
        if password_hash and check_password_hash(password_hash[0], password):
            return True
        else:
            return False

# 会员注册函数
def register(username, password):
    if not authenticate(username, password):
        password_hash = make_password_hash(password)
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO members (username, password_hash) VALUES (?, ?)", (username, password_hash))
            conn.commit()
            return True
    return False

# CherryPy配置
class MemberManagement(object):
    """会员管理系统的CherryPy暴露类"""
    @cherrypy.expose
    def index(self):
        return "Welcome to the Member Management System"
    """主页，返回欢迎信息"""

    @cherrypy.expose
    def login(self, username, password):
        if authenticate(username, password):
            cherrypy.session['username'] = username
            return "Login successful"
        else:
            return "Login failed"
        """登录接口"""

    @cherrypy.expose
    def logout(self):
        if 'username' in cherrypy.session:
            del cherrypy.session['username']
        return "Logged out"
        """登出接口"""

    @cherrypy.expose
    def register(self, username, password):
        if register(username, password):
            return "Registration successful"
        else:
            return "Registration failed"
        """注册接口"""

# 初始化数据库和CherryPy引擎
def start_server():
    init_db()
    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 8080})
    cherrypy.quickstart(MemberManagement())
    """启动CherryPy服务器"""

if __name__ == '__main__':
    start_server()
    """程序入口点，启动服务器"""

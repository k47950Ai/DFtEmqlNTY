# 代码生成时间: 2025-08-23 08:22:35
import cherrypy
import random
import string

# 定义一个简单的测试数据生成器
class TestDataGenerator:
    """Generates random test data for various types."""

    @cherrypy.expose
    def generate_random_string(self, length=10):
        """Generates a random string of given length."""
        try:
            if length < 1:
                raise ValueError("Length must be greater than 0.")
            return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
        except ValueError as e:
            return str(e)

    @cherrypy.expose
    def generate_random_number(self, min_value=1, max_value=100):
        """Generates a random number within the given range."""
        try:
            if min_value >= max_value:
                raise ValueError("Min value must be less than max value.")
            return random.randint(min_value, max_value)
        except ValueError as e:
            return str(e)

    @cherrypy.expose
    def generate_random_email(self):
        """Generates a random email address."""
        try:
            domain = f"{random.choice(string.ascii_lowercase)}.com"
            username = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
            return f"{username}@{domain}"
        except Exception as e:
            return str(e)

# 设置CherryPy服务器配置
config = {
    'global': {
        'server.socket_host': '127.0.0.1',
        'server.socket_port': 8080,
    },
    '/test_data': {
        'tools.sessions.on': True,
        'tools.response_headers.on': True,
        'tools.response_headers.headers': [('Content-Type', 'application/json')]
    },
}

# 启动CherryPy服务器
if __name__ == '__main__':
    cherrypy.quickstart(TestDataGenerator(), config=cherrypy.config.update({'/': config}))
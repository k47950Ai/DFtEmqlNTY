# 代码生成时间: 2025-08-07 07:16:10
import cherrypy
from cherrypy import tools
from cherrypy.lib import json_respond
import json

# 数据模型
class UserModel:
    def __init__(self, data):
        """
        数据模型初始化方法，用于接收用户数据并初始化用户模型。
        :param data: 用户数据，包含用户信息的字典。
        """
        self.id = data.get('id')
        self.name = data.get('name')
        self.email = data.get('email')

    def to_dict(self):
        """
        将用户模型转换为字典，以便序列化。
        :return: 用户信息的字典。
        """
        return {'id': self.id, 'name': self.name, 'email': self.email}


# 服务类
class UserService:
    def __init__(self):
        """
        用户服务类初始化方法，用于初始化用户服务。
        """
        self.users = {}  # 使用字典存储用户数据

    def add_user(self, user_model):
        """
        添加用户方法，用于将用户模型添加到用户服务中。
        :param user_model: 用户模型实例。
        """
        if user_model.id in self.users:
            raise Exception('User already exists')
        self.users[user_model.id] = user_model
        return user_model.to_dict()

    def get_user(self, user_id):
        """
        获取用户方法，用于根据用户ID获取用户信息。
        :param user_id: 用户ID。
        :return: 用户信息的字典。
        """
        user_model = self.users.get(user_id)
        if not user_model:
            raise Exception('User not found')
        return user_model.to_dict()

# CherryPy配置
conf = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 8080,
    }
}

# CherryPy暴露的服务
class Root:
    def __init__(self):
        self.user_service = UserService()

    @cherrypy.expose
    def add_user(self, id=None, name=None, email=None):
        """
        添加用户接口，用于接收用户数据并添加用户。
        :param id: 用户ID。
        :param name: 用户名称。
        :param email: 用户邮箱。
        """
        if not all([id, name, email]):
            return json.dumps({'error': 'Missing parameters'})
        user_data = {'id': id, 'name': name, 'email': email}
        user_model = UserModel(user_data)
        try:
            result = self.user_service.add_user(user_model)
        except Exception as e:
            return json.dumps({'error': str(e)})
        return json.dumps({'data': result})

    @cherrypy.expose
    def get_user(self, user_id=None):
        """
        获取用户接口，用于根据用户ID获取用户信息。
        :param user_id: 用户ID。
        """
        if not user_id:
            return json.dumps({'error': 'Missing parameters'})
        try:
            result = self.user_service.get_user(user_id)
        except Exception as e:
            return json.dumps({'error': str(e)})
        return json.dumps({'data': result})

if __name__ == '__main__':
    cherrypy.quickstart(Root(), config=conf)
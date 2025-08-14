# 代码生成时间: 2025-08-14 20:29:03
import cherrypy
import json
import os
from cherrypy.lib import static

"""
配置文件管理器，用于处理配置文件的读取、更新和删除。
"""

class ConfigManager:
    def __init__(self, config_dir):
        """
        初始化配置文件管理器。

        :param config_dir: 配置文件所在的目录
        """
        self.config_dir = config_dir
        self.config_files = self._load_config_files()

    def _load_config_files(self):
        """
        加载配置目录中的所有配置文件。

        :return: 配置文件字典
        """
        config_files = {}
        for filename in os.listdir(self.config_dir):
            if filename.endswith('.json'):
                file_path = os.path.join(self.config_dir, filename)
                with open(file_path, 'r') as file:
                    config_files[filename] = json.load(file)
        return config_files

    def get_config(self, filename):
        """
        获取指定配置文件的内容。

        :param filename: 配置文件名
        :return: 配置内容
        """
        if filename in self.config_files:
            return self.config_files[filename]
        else:
            raise FileNotFoundError(f'配置文件 {filename} 不存在')

    def update_config(self, filename, config_data):
        """
        更新指定配置文件的内容。

        :param filename: 配置文件名
        :param config_data: 新的配置数据
        :return: 更新后的配置内容
        """
        if filename in self.config_files:
            file_path = os.path.join(self.config_dir, filename)
            with open(file_path, 'w') as file:
                json.dump(config_data, file, indent=4)
            self.config_files[filename] = config_data
            return config_data
        else:
            raise FileNotFoundError(f'配置文件 {filename} 不存在')

    def delete_config(self, filename):
        """
        删除指定配置文件。

        :param filename: 配置文件名
        """
        if filename in self.config_files:
            os.remove(os.path.join(self.config_dir, filename))
            del self.config_files[filename]
        else:
            raise FileNotFoundError(f'配置文件 {filename} 不存在')


def main():
    """
    主函数，启动CherryPy服务器。
    """
    config_dir = 'configs'  # 配置文件目录
    config_manager = ConfigManager(config_dir)

    # 配置CherryPy服务器
    cherrypy.config.update(
        {'server.socket_host': '0.0.0.0', 'server.socket_port': 8080}
    )

    # 配置路由
    cherrypy.tree.mount(
        {
            'get_config': config_manager.get_config,
            'update_config': config_manager.update_config,
            'delete_config': config_manager.delete_config
        },
        '/config',
        {
            'get_config': {'method': ['GET']},
            'update_config': {'method': ['POST']},
            'delete_config': {'method': ['DELETE']}
        }
    )

    # 启动服务器
    cherrypy.engine.start()
    cherrypy.engine.block()

if __name__ == '__main__':
    main()
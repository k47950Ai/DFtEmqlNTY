# 代码生成时间: 2025-08-28 17:45:41
import os
import shutil
from cherrypy import暴露

# 文件夹结构整理器配置
class FolderOrganizer:
    def __init__(self, source_dir, target_dir):
        self.source_dir = source_dir
        self.target_dir = target_dir

    def organize(self):
        """整理文件夹结构"""
        if not os.path.exists(self.source_dir):
            raise ValueError(f"源文件夹{self.source_dir}不存在")
        
        if not os.path.exists(self.target_dir):
            raise ValueError(f"目标文件夹{self.target_dir}不存在")
        
        for root, dirs, files in os.walk(self.source_dir):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                relative_path = os.path.relpath(file_path, self.source_dir)
                target_path = os.path.join(self.target_dir, relative_path)
                target_dir = os.path.dirname(target_path)
                
                # 确保目标文件夹存在
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)
                
                # 移动文件
                shutil.move(file_path, target_path)

# CherryPy配置和路由
class Root:
    def index(self):
        """首页路由"""
        return "欢迎使用文件夹结构整理器"

    @暴露("/organize")
    def organize_folder(self, source, target):
        """处理文件整理请求"""
        try:
            organizer = FolderOrganizer(source, target)
            organizer.organize()
            return f"文件从{source}整理到{target}完成"
        except Exception as e:
            return f"发生错误: {str(e)}"

if __name__ == '__main__':
    # CherryPy配置
    cherrypy.config.update({'server.socket_host': '0.0.0.0',
                             'server.socket_port': 8080})
    cherrypy.quickstart(Root())
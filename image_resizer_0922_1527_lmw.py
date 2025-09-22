# 代码生成时间: 2025-09-22 15:27:39
import os
from cherrypy import expose, File
from PIL import Image
import logging

# 设置日志记录
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ImageResizer:
    """
    图片尺寸批量调整器，使用CHERRYPY框架提供服务。
    """
    def __init__(self):
        # 存储上传的图片
        self.uploaded_images = []

    @expose
    def index(self):
        """
        主页，提供上传图片的表单。
        """
        return "<html><body><form action='/upload' method='post' enctype='multipart/form-data'>
Image: <input type='file' name='image'><br>
<input type='submit' value='Resize'></form></body></html>"

    @expose
    def upload(self, image=None):
        """
        处理上传的图片并存储。
        """
        if image:
            self.uploaded_images.append(image.filename)
            return "Image uploaded successfully."
        else:
            return "No image uploaded."

    @expose
    def resize(self, filename=None, new_width=None, new_height=None):
        """
        调整图片尺寸。
        """
        if not filename or not new_width or not new_height:
            return "Missing parameters."
        if filename not in self.uploaded_images:
            return "Image not found."
        try:
            # 打开图片
            img = Image.open('uploaded_images/' + filename)
            # 调整尺寸
            img = img.resize((int(new_width), int(new_height)), Image.ANTIALIAS)
            # 保存调整后的图片
            img.save('resized_images/' + filename)
            return "Image resized successfully."
        except Exception as e:
            logger.error(f"Failed to resize image: {e}")
            return "Failed to resize image."

# 主程序
if __name__ == '__main__':
    # 创建上传和保存图片的目录
    os.makedirs('uploaded_images', exist_ok=True)
    os.makedirs('resized_images', exist_ok=True)
    # 配置CHERRYPY服务器
    conf = {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 8080,
    }
    cherrypy.quickstart(ImageResizer(), '/', config=conf)
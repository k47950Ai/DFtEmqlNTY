# 代码生成时间: 2025-09-07 02:33:09
import os
from cherrypy import暴露异常, tools, HTTPError
from cherrypy.lib import file_generator
from PIL import Image
from io import BytesIO
import logging

# 设置日志记录器
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ImageResizer:
    """
    图片尺寸批量调整器：提供一个web服务，允许用户上传图片，并调整图片尺寸。
    """
    exposed = True

    def index(self):
        """
        首页路由，返回上传表单。
        """
        return """
        <html><body>
        <h2>Image Resizer</h2>
        <form action="/resize" method="post" enctype="multipart/form-data">
        <input type="file" name="image" accept="image/*"/>
        <input type="text" name="width" placeholder="Width"/>
        <input type="text" name="height" placeholder="Height"/>
        <input type="submit" value="Resize Image"/>
        </form>
        </body></html>
        """

    def resize(self, image=None, width=None, height=None):
        """
        处理图片尺寸调整。
        """
        if image is None or width is None or height is None:
            raise HTTPError(400, "Missing parameters.")
        try:
            # 读取图片
            image_file = image.file.read()
            image = Image.open(BytesIO(image_file))
            # 调整尺寸
            resized_image = image.resize((int(width), int(height)), Image.ANTIALIAS)
            # 创建响应体
            out = BytesIO()
            resized_image.save(out, format=image.format)
            out.seek(0)
            return file_generator(out, image.type, filename="resized_image." + image.format.lower())
        except Exception as e:
            logger.error(f"Error resizing image: {e}")
            raise HTTPError(500, "Error resizing image.")

    def upload(self, image=None):
        """
        处理图片上传。
        """
        if image is None:
            raise HTTPError(400, "No image uploaded.")
        try:
            # 保存上传的图片
            image_path = os.path.join("uploads", image.filename)
            with open(image_path, "wb") as f:
                f.write(image.file.read())
            return f"Image uploaded successfully to {image_path}"
        except Exception as e:
            logger.error(f"Error uploading image: {e}")
            raise HTTPError(500, "Error uploading image.")

# 设置CherryPy配置
config = {
    "server.socket_host": "0.0.0.0",
    "server.socket_port": 8080,
    "/": {
        "tools.staticdir.root": os.path.abspath(os.getcwd()),
    },
}

if __name__ == "__main__":
    from cherrypy import quickstart
    quickstart(ImageResizer(), config=config)
# 代码生成时间: 2025-08-08 12:48:28
import cherrypy
import hashlib
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# 密码加密解密工具类
class PasswordTool:
    def __init__(self):
        self.key = get_random_bytes(16)  # AES密钥长度为16字节

    # 加密方法
    def encrypt(self, password):
        """加密密码"""
        try:
            iv = get_random_bytes(AES.block_size)  # 初始化向量
            cipher = AES.new(self.key, AES.MODE_CBC, iv)
            padded_data = pad(password.encode('utf-8'), AES.block_size)
            encrypted_password = base64.b64encode(iv + cipher.encrypt(padded_data)).decode('utf-8')
            return encrypted_password
        except Exception as e:
            raise ValueError(f"加密失败: {str(e)}")

    # 解密方法
    def decrypt(self, encrypted_password):
        """解密密码"""
        try:
            encrypted_password_bytes = base64.b64decode(encrypted_password)
            iv = encrypted_password_bytes[:AES.block_size]
            cipher = AES.new(self.key, AES.MODE_CBC, iv)
            padded_data = cipher.decrypt(encrypted_password_bytes[AES.block_size:])
            password = unpad(padded_data, AES.block_size).decode('utf-8')
            return password
        except Exception as e:
            raise ValueError(f"解密失败: {str(e)}")

# CherryPy服务
class PasswordToolService:
    def __init__(self):
        self.tool = PasswordTool()

    # 加密接口
    @cherrypy.expose
    def encrypt(self, password):
        "
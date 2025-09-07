# 代码生成时间: 2025-09-07 20:59:18
import cherrypy
import hashlib
import base64
from getpass import getpass

# 密码加密解密工具
class PasswordEncryptionTool:
    """
    A simple tool for encrypting and decrypting passwords using CherryPy framework.

    Attributes:
        None
    """

    @cherrypy.expose
    def index(self):
        """
        The main page of the tool.
        """
        return "Welcome to Password Encryption Tool"

    @cherrypy.expose
    def encrypt(self, password):
        """
        Encrypts a given password.

        Args:
            password (str): The password to be encrypted.

        Returns:
            str: The encrypted password.
        """
        try:
            hashed_password = self._encrypt_password(password)
            return f"Encrypted Password: {hashed_password}"
        except Exception as e:
            return f"Error: {str(e)}"

    @cherrypy.expose
    def decrypt(self, hashed_password):
        """
        Decrypts a given hashed password.

        Args:
            hashed_password (str): The hashed password to be decrypted.

        Returns:
            str: The decrypted password.
        """
        try:
            decrypted_password = self._decrypt_password(hashed_password)
            return f"Decrypted Password: {decrypted_password}"
        except Exception as e:
            return f"Error: {str(e)}"

    def _encrypt_password(self, password):
        """
        Helper function to encrypt the password.

        Args:
            password (str): The password to be encrypted.

        Returns:
            str: The encrypted password.
        """
        salt = base64.b64encode(os.urandom(16)).decode('utf-8')
        hashed_password = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
        return f"{hashed_password}:{salt}"

    def _decrypt_password(self, hashed_password):
        """
        Helper function to decrypt the password.

        Args:
            hashed_password (str): The hashed password to be decrypted.

        Returns:
            str: The decrypted password.
        """
        if ':' not in hashed_password:
            raise ValueError("Invalid hashed password format")
        hashed, salt = hashed_password.split(':', 1)
        return hashlib.sha256((hashed[:len(hashed) - len(salt)] + salt).encode('utf-8')).hexdigest()

if __name__ == '__main__':
    conf = {
        'global': {
            'server.socket_port': 8080,
            'server.socket_host': '127.0.0.1'
        }
    }
    cherrypy.quickstart(PasswordEncryptionTool(), '/', config=conf)
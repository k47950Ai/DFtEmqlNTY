# 代码生成时间: 2025-08-20 00:07:54
import cherrypy
from cherrypy.lib import sessions
from cherrypy.process.plugins import Monitor

# 数据存储结构
inventory = {
    'items': [],
    'transactions': []
}

class InventoryManager:
    """库存管理系统。"""

    @cherrypy.expose
    def index(self):
        """主页，显示库存列表。"""
        return 'Welcome to the Inventory Management System!'

    @cherrypy.expose
    def add_item(self, item_name, quantity):
        """添加库存项。"""
        try:
            if quantity <= 0:
                raise ValueError('Quantity must be greater than zero.')
            inventory['items'].append({'name': item_name, 'quantity': int(quantity)})
            return 'Item added successfully.'
        except Exception as e:
            return str(e)

    @cherrypy.expose
    def remove_item(self, item_name):
        """移除库存项。"""
        try:
            for item in inventory['items']:
                if item['name'] == item_name:
                    inventory['items'].remove(item)
                    return 'Item removed successfully.'
            return 'Item not found.'
        except Exception as e:
            return str(e)

    @cherrypy.expose
    def update_quantity(self, item_name, quantity):
        """更新库存项数量。"""
        try:
            if quantity <= 0:
                raise ValueError('Quantity must be greater than zero.')
            for item in inventory['items']:
                if item['name'] == item_name:
                    item['quantity'] = int(quantity)
                    return 'Quantity updated successfully.'
            return 'Item not found.'
        except Exception as e:
            return str(e)

    @cherrypy.expose
    def get_inventory(self):
        """获取整个库存列表。"""
        return inventory

    @cherrypy.expose
    def record_transaction(self, item_name, quantity):
        """记录库存交易。"""
        try:
            if quantity <= 0:
                raise ValueError('Quantity must be greater than zero.')
            transaction = {'item': item_name, 'quantity': int(quantity)}
            inventory['transactions'].append(transaction)
            return 'Transaction recorded successfully.'
        except Exception as e:
            return str(e)

if __name__ == '__main__':
    # 配置CherryPy服务器
    conf = {
        'global': {
            'server.socket_host': '127.0.0.1',
            'server.socket_port': 8080,
        },
        '/': {
            'tools.sessions.on': True,  # 启用会话
            'tools.sessions.timeout': 60,  # 会话超时时间（秒）
        },
    }
    cherrypy.quickstart(InventoryManager(), '/', conf)

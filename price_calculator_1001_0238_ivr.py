# 代码生成时间: 2025-10-01 02:38:20
import cherrypy

# 定义价格计算类
class PriceCalculator:
    def __init__(self):
        """初始化价格计算引擎"""
        self.tax_rate = 0.08  # 默认税率为8%

    def calculate_price(self, amount, tax_rate=None):
        """计算商品价格（含税）"""
        if tax_rate is None:
            tax_rate = self.tax_rate
        if amount < 0:
            raise ValueError("金额不能为负数")
        tax = amount * tax_rate
        total_price = amount + tax
        return total_price

# 配置CherryPy服务器
def config():
    cherrypy.config.update({
        'server.socket_host': '127.0.0.1',
        'server.socket_port': 8080,
    })

def get_price(amount, tax_rate=None):
    """计算并返回商品价格（含税）"""
    try:
        calculator = PriceCalculator()
        price = calculator.calculate_price(amount, tax_rate)
        return {"success": True, "price": price}
    except ValueError as e:
        return {"success": False, "error": str(e)}

# 设置CherryPy路由和启动服务器
def setup_routes():
    cherrypy.tree.mount(get_price, '/api/price', {'methods': ['GET']})
    cherrypy.config.update(
        {'tools.trailing_slash.on': True}
    )

if __name__ == '__main__':
    config()
    setup_routes()
    cherrypy.engine.start()
    cherrypy.engine.block()
# 代码生成时间: 2025-09-09 05:41:13
import cherrypy
from jinja2 import Template
import json

# 定义一个全局变量来存储图表的数据
chart_data = {}

# 定义路由和视图函数
class InteractiveChartGenerator:
    '''
    交互式图表生成器
    """
    def index(self):
        # 返回一个HTML页面，包含一个表单来提交图表数据
        return Template("""
            <html>
            <body>
                <form method="post" action="/generate_chart">
                    <label for="data">图表数据（JSON格式）:</label>
                    <textarea id="data" name="data"></textarea>
                    <button type="submit">生成图表</button>
                </form>
            </body>
            </html>
            """).render()

    def generate_chart(self):
        try:
            # 从表单数据中获取图表数据
            data = cherrypy.request.form['data']
            # 解析JSON数据
            chart_data = json.loads(data)
            # 验证图表数据
            if not isinstance(chart_data, dict):
                raise ValueError("图表数据必须是字典类型")
            if 'x' not in chart_data or 'y' not in chart_data:
                raise ValueError("图表数据必须包含'x'和'y'键")
            # 生成图表HTML代码
            chart_html = Template("""
                <html>
                <body>
                    <canvas id="chart"></canvas>
                    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
                    <script>
                        const ctx = document.getElementById('chart').getContext('2d');
                        const chart = new Chart(ctx, {
                            type: 'line',
                            data: {
                                labels: {{ x | tojson }},
                                datasets: [{
                                    label: '示例图表',
                                    data: {{ y | tojson }},
                                    borderColor: 'rgb(75, 192, 192)',
                                    tension: 0.1
                                }]
                            },
                            options: {}
                        });
                    </script>
                </body>
                </html>
                """).render(x=chart_data['x'], y=chart_data['y'])
            return chart_html
        except json.JSONDecodeError:
            return "无效的JSON格式"
        except ValueError as e:
            return str(e)

# 配置CherryPy服务器
cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 8080})

# 启动CherryPy服务器
if __name__ == '__main__':
    cherrypy.quickstart(InteractiveChartGenerator())
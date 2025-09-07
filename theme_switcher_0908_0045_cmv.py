# 代码生成时间: 2025-09-08 00:45:44
import cherrypy

class ThemeSwitcher:
    def __init__(self):
        # 默认主题设置为'light'
        self.default_theme = 'light'
        self.current_theme = self.default_theme

    def set_theme(self, theme):
        """
        设置当前主题
        :param theme: str - 新的主题名称
        """
        if theme in ['light', 'dark']:
            self.current_theme = theme
        else:
            # 如果请求的主题不在允许的列表中，返回错误信息
            raise cherrypy.HTTPError(400, "Invalid theme")

    def get_theme(self):
        """
        获取当前主题
        """
        return self.current_theme

    @cherrypy.expose
    def switch_theme(self, new_theme):
        """
        HTTP端点，用于切换主题
        :param new_theme: str - 要切换到的主题
        """
        try:
            self.set_theme(new_theme)
            return f"Theme switched to {self.current_theme}"
        except cherrypy.HTTPError as e:
            return str(e)

    @cherrypy.expose
    def current_theme(self):
        """
        HTTP端点，返回当前主题
        """
        return f"The current theme is {self.current_theme}"

if __name__ == '__main__':
    cherrypy.quickstart(ThemeSwitcher())

# 代码生成时间: 2025-08-10 11:51:49
import cherrypy
def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract two numbers."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide two numbers.
    Raises ValueError if the divisor is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

class MathCalculator:
    """A class providing a set of mathematical operations."""
    @cherrypy.expose
    def add(self, a, b):
        """Add two numbers and return the result."""
        return str(add(a, b))
    
    @cherrypy.expose
    def subtract(self, a, b):
        """Subtract two numbers and return the result."""
        return str(subtract(a, b))
    
    @cherrypy.expose
    def multiply(self, a, b):
        """Multiply two numbers and return the result."""
        return str(multiply(a, b))
    
    @cherrypy.expose
    def divide(self, a, b):
        """Divide two numbers and return the result or error message."""
        try:
            return str(divide(a, b))
        except ValueError as e:
            return str(e)

if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher()
        }
    }
    cherrypy.quickstart(MathCalculator(), '/', conf)
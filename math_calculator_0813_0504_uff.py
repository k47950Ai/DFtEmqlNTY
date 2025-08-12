# 代码生成时间: 2025-08-13 05:04:11
import cherrypy
def add(a, b):
    """Add two numbers."""
    try:       
        return float(a) + float(b)
    except ValueError:       
        raise cherrypy.HTTPError(400, 'Invalid input: expected numbers.')

def subtract(a, b):
    """Subtract two numbers."""
    try:       
        return float(a) - float(b)
    except ValueError:       
        raise cherrypy.HTTPError(400, 'Invalid input: expected numbers.')

def multiply(a, b):
    """Multiply two numbers."""
    try:       
        return float(a) * float(b)
    except ValueError:       
        raise cherrypy.HTTPError(400, 'Invalid input: expected numbers.')

def divide(a, b):
    """Divide two numbers."""
    try:       
        if b == 0:         
            raise cherrypy.HTTPError(400, 'Invalid input: division by zero.')       
        return float(a) / float(b)
    except ValueError:       
        raise cherrypy.HTTPError(400, 'Invalid input: expected numbers.')

def power(a, b):
    """Raise a number to a power."""
    try:       
        return float(a) ** float(b)
    except ValueError:       
        raise cherrypy.HTTPError(400, 'Invalid input: expected numbers.')

def main():
    cherrypy.quickstart):
        cherrypy.tools.json_out = cherrypy.Tool('before_finalize', lambda v: v, content_type='application/json')
        @cherrypy.expose()
        def index():
            return 'Welcome to the Math Calculator!'
        @cherrypy.expose()
        def calculate(operation, a, b):  # operation: add, subtract, multiply, divide, power
            operations = {
                'add': add,
                'subtract': subtract,
                'multiply': multiply,
                'divide': divide,
                'power': power
            }
            if operation not in operations:
                raise cherrypy.HTTPError(404, 'Invalid operation.')
            result = operations[operation](a, b)
            return {"result": result}
if __name__ == '__main__':
    main()
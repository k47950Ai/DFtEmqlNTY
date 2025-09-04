# 代码生成时间: 2025-09-04 12:41:47
import cherrypy
def add(a, b):
    """Add two numbers."""
    try:
        result = a + b
    except TypeError:
        raise cherrypy.HTTPError(400, 'Invalid input types for addition.')
    return str(result)

def subtract(a, b):
    """Subtract two numbers."""
    try:
        result = a - b
    except TypeError:
        raise cherrypy.HTTPError(400, 'Invalid input types for subtraction.')
    return str(result)

def multiply(a, b):
    """Multiply two numbers."""
    try:
        result = a * b
    except TypeError:
        raise cherrypy.HTTPError(400, 'Invalid input types for multiplication.')
    return str(result)

def divide(a, b):
    """Divide two numbers."""
    try:
        result = a / b
    except TypeError:
        raise cherrypy.HTTPError(400, 'Invalid input types for division.')
    except ZeroDivisionError:
        raise cherrypy.HTTPError(400, 'Cannot divide by zero.')
    return str(result)

def square(a):
    """Square a number."""
    try:
        result = a ** 2
    except TypeError:
        raise cherrypy.HTTPError(400, 'Invalid input type for squaring.')
    return str(result)

def square_root(a):
    """Calculate the square root of a number."""
    try:
        result = a ** 0.5
    except TypeError:
        raise cherrypy.HTTPError(400, 'Invalid input type for square root.')
    except ValueError:
        raise cherrypy.HTTPError(400, 'Cannot calculate square root of a negative number.')
    return str(result)
# CherryPy configuration
cherrypy.tree.mount(add, '/add', {'a': 0, 'b': 0})
cherrypy.tree.mount(subtract, '/subtract', {'a': 0, 'b': 0})
cherrypy.tree.mount(multiply, '/multiply', {'a': 0, 'b': 0})
cherrypy.tree.mount(divide, '/divide', {'a': 0, 'b': 0})
cherrypy.tree.mount(square, '/square', {'a': 0})
cherrypy.tree.mount(square_root, '/square_root', {'a': 0})
if __name__ == '__main__':
    cherrypy.quickstart()
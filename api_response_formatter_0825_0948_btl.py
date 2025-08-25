# 代码生成时间: 2025-08-25 09:48:40
import cherrypy
def api_response(status_code, data, message=None):\
    """Formats API responses with a status code, data, and an optional message."""
    # Prepare the response dictionary
    response = {"status_code": status_code, "data": data}
    
    # If a message is provided, add it to the response dictionary
    if message:
        response["message"] = message
    
    # Return the formatted response
    return response

def error_handler(error, error_code, message):\
    """Handles errors by returning a formatted error response."""
    # Log the error (this could be replaced with actual logging logic)
    print(f"Error {error_code}: {message}, Original error: {error}")
    
    # Return the error response
    return api_response(error_code, {}, message)

def main():
    # CherryPy configuration
    cherrypy.quickstart(Root())

class Root:
    """Root class for CherryPy application."""
    @cherrypy.expose
    def index(self):
        """Homepage route."""
        return "Welcome to the API Response Formatter Tool!"

    @cherrypy.expose
    def format_response(self, status_code, data, message=None):
        """Endpoint to format API responses."""
        try:
            # Convert input parameters to appropriate types
            status_code = int(status_code)
            data = eval(data)  # Use eval with caution; consider using json.loads() for安全性
            
            # Format the response using the api_response function
            return api_response(status_code, data, message)
        except Exception as e:
            # Handle any exceptions that occur during response formatting
            return error_handler(e, 500, "Internal Server Error")

def run():
    main()

def test():
    from cherrypy.test import helper
    # Test the format_response endpoint
    class Test(helper.CPWebCase):
        def test_format_response(self):
            self.getPage("/format_response?status_code=200&data={\\"key\\": \\"value\\"}&message=Success")
            self.assertStatus(200)
            self.assertBody("""{\
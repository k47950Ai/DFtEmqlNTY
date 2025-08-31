# 代码生成时间: 2025-08-31 13:34:03
import cherrypy
def setup_server():
    # Setup the CherryPy server
    cherrypy.config.update({'server.socket_host': '127.0.0.1', 'server.socket_port': 8080})
    class Root:
        def index(self):
            return "Hello, World!"
    root = Root()
    cherrypy.tree.mount(root, '/')

def start_server():
    # Start the CherryPy server
    cherrypy.engine.start()
    cherrypy.engine.block()

def test_root_index():
    # Test the root index
    from cherrypy.test import helper
    from cherrypy.test import test
    test.webtest.WebCase("/").run()
    assert cherrypy.response.status == 200

def main():
    # Main function to setup and start the server or run tests
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test_root_index()
    else:
        setup_server()
        start_server()

if __name__ == "__main__":
    main()

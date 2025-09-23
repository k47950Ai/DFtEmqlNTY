# 代码生成时间: 2025-09-23 09:55:01
import cherrypy
def get_page_content(url):
    """
    Fetch the content of a webpage.
    Args:
        url (str): The URL of the webpage to fetch.
    Returns:
        str: The content of the webpage as a string.
    Raises:
        Exception: If there is an issue fetching the webpage.
    """
    try:
        # Importing the required modules within the function to keep the script clean
        from urllib.request import urlopen
        from urllib.error import URLError

        # Opening the URL and reading the content
        with urlopen(url) as response:
            return response.read().decode('utf-8')
    except URLError as e:
        raise Exception(f"Failed to retrieve content: {e.reason}")

class WebScraper:
    """
    A CherryPy application to scrape web content.
    """
    @cherrypy.expose
    def index(self):
        """
        The main page of the application.
        Displays a form to input the URL.
        """
        return """
        <html><body>
        <h1>Web Scraper</h1>
        <form action="/scrape" method="post">
            <input type="text" name="url" placeholder="Enter URL here" required/>
            <input type="submit" value="Scrape!"/>
        </form>
        </body></html>
        """

    @cherrypy.expose
    def scrape(self, url):
        """
        Scrapes the content of the webpage at the provided URL.
        Args:
            url (str): The URL to scrape.
        Returns:
            str: The content of the webpage.
        """
        try:
            content = get_page_content(url)
            return f"<h1>Content of {url}</h1><p>{content}</p>"
        except Exception as e:
            return f"<h1>Error</h1><p>{e}</p>"

if __name__ == '__main__':
    # Configuring CherryPy to serve the application
    cherrypy.config.update({'server.socket_host': '0.0.0.0',
                            'server.socket_port': 8080})
    cherrypy.quickstart(WebScraper())
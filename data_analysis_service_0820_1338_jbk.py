# 代码生成时间: 2025-08-20 13:38:38
import cherrypy
def get_statistics(data):
    """
    Function to calculate statistics of a given dataset.

    Args:
        data (list): A list of numerical values.

    Returns:
        dict: A dictionary containing statistics such as mean, median, and standard deviation.
    """
    try:
        if not data:
            raise ValueError("Data list is empty.")
        mean = sum(data) / len(data)
        median = sorted(data)[len(data) // 2] if len(data) % 2 != 0 else \
            (sorted(data)[len(data) // 2 - 1] + sorted(data)[len(data) // 2]) / 2
        stdev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
        return {"mean": mean, "median": median, "stdev": stdev}
    except TypeError:
        raise ValueError("Data list must contain only numbers.")
    except Exception as e:
        raise e

class DataAnalysisService:
    """
    A CherryPy service class to handle data analysis requests.
    """
    @cherrypy.expose
    def index(self):
        """
        The index page for the CherryPy service.
        """
        return "Welcome to the Data Analysis Service."

    @cherrypy.expose
    def calculate(self, data):
        """
        A CherryPy method to calculate and return the statistics of a dataset.

        Args:
            data (str): A JSON string containing a list of numbers.

        Returns:
            str: A JSON string containing the calculated statistics.
        """
        try:
            data_list = [float(item) for item in data.split(",")]
            statistics = get_statistics(data_list)
            return "{"mean": "{mean}", "median": "{median}", "stdev": "{stdev}"}".format(
                **statistics
            )
        except ValueError as ve:
            return "{"error": "{error}"}".format(error=str(ve))
        except Exception as e:
            return "{"error": "{error}"}".format(error=str(e))

if __name__ == '__main__':
    conf = {
        'global': {'server.socket_host': '127.0.0.1',
                  'server.socket_port': 8080},
    }
    cherrypy.quickstart(DataAnalysisService(), '/', conf)
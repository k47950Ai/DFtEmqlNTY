# 代码生成时间: 2025-08-05 00:04:55
import cherrypy
def bubble_sort(data):
    """
    Sorts a list of numbers using the Bubble Sort algorithm.
    
    Args:
    data (list): A list of numbers to be sorted.
    
    Returns:
    list: A sorted list of numbers.
    """
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1] :
                data[j], data[j+1] = data[j+1], data[j]
    return data
def quick_sort(data):
    """
    Performs a quicksort on a list of numbers.
    
    Args:
    data (list): A list of numbers to be sorted.
    
    Returns:
    list: A sorted list of numbers.
    """
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        small_elements = [el for el in data[1:] if el <= pivot]
        large_elements = [el for el in data[1:] if el > pivot]
        return quick_sort(small_elements) + [pivot] + quick_sort(large_elements)class SortingService:
    """
    A CherryPy service that provides sorting algorithms.
    """
    @cherrypy.expose
    def sort(self, data, algorithm='quick_sort'):
        """
        Returns a sorted list based on the selected algorithm.
        
        Args:
        data (str): A JSON string of a list of numbers.
        algorithm (str): The sorting algorithm to use. Defaults to 'quick_sort'.
        
        Returns:
        str: A JSON string of the sorted list.
        """
        try:
            data_list = [int(i) for i in data.split(',')]
        except ValueError:
            return json.dumps({'error': 'Invalid input data'})
        
        if algorithm == 'quick_sort':
            sorted_list = quick_sort(data_list)
        elif algorithm == 'bubble_sort':
            sorted_list = bubble_sort(data_list)
        else:
            return json.dumps({'error': 'Sorting algorithm not supported'})
        
        return json.dumps({'sorted_list': sorted_list})if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '127.0.0.1',
                         'server.socket_port': 8080})
    cherrypy.quickstart(SortingService())
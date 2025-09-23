# 代码生成时间: 2025-09-24 00:30:50
import cherrypy
def bubble_sort(arr):
    """
    A simple implementation of the Bubble Sort algorithm.
    This function takes a list of numbers and sorts them in ascending order.
    :param arr: List of numbers to be sorted.
    :return: A sorted list of numbers.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
def insertion_sort(arr):
    """
    A simple implementation of the Insertion Sort algorithm.
    This function takes a list of numbers and sorts them in ascending order.
    :param arr: List of numbers to be sorted.
    :return: A sorted list of numbers.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
def quick_sort(arr):
    """
    A simple implementation of the Quick Sort algorithm.
    This function takes a list of numbers and sorts them in ascending order.
    :param arr: List of numbers to be sorted.
    :return: A sorted list of numbers.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)
def sort_algorithms(exposed=True):
    """
    A CherryPy page handler that exposes the sorting algorithms.
    It provides endpoints for each sorting algorithm.
    :param exposed: A boolean indicating whether the page handler is exposed.
    """
    @cherrypy.expose
    def bubble(self, arr):
        """
        An endpoint for the Bubble Sort algorithm.
        It takes a list of numbers as input and returns the sorted list.
        :param arr: A string representation of a list of numbers to be sorted.
        :return: A sorted list of numbers as a JSON response.
        """
        try:
            arr = eval(arr)
            sorted_arr = bubble_sort(arr)
            return {'status': 'success', 'sorted_arr': sorted_arr}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    @cherrypy.expose
    def insertion(self, arr):
        """
        An endpoint for the Insertion Sort algorithm.
        It takes a list of numbers as input and returns the sorted list.
        :param arr: A string representation of a list of numbers to be sorted.
        :return: A sorted list of numbers as a JSON response.
        """
        try:
            arr = eval(arr)
            sorted_arr = insertion_sort(arr)
            return {'status': 'success', 'sorted_arr': sorted_arr}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    @cherrypy.expose
    def quick(self, arr):
        """
        An endpoint for the Quick Sort algorithm.
        It takes a list of numbers as input and returns the sorted list.
        :param arr: A string representation of a list of numbers to be sorted.
        :return: A sorted list of numbers as a JSON response.
        """
        try:
            arr = eval(arr)
            sorted_arr = quick_sort(arr)
            return {'status': 'success', 'sorted_arr': sorted_arr}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    if exposed:
        cherrypy.expose(bubble)
        cherrypy.expose(insertion)
        cherrypy.expose(quick)
    return {"bubble": bubble, "insertion": insertion, "quick": quick}
if __name__ == '__main__':
    cherrypy.quickstart(sort_algorithms())
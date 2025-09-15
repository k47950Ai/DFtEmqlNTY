# 代码生成时间: 2025-09-15 08:38:40
import cherrypy
def bubble_sort(numbers):
    """Performs bubble sort on a list of numbers.

    Args:
        numbers (list): A list of numbers to be sorted.

    Returns:
        list: The sorted list of numbers.

    Raises:
        TypeError: If input is not a list or contains non-numeric elements.
    """
    if not isinstance(numbers, list) or not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("Input must be a list of numbers.")

    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers
def selection_sort(numbers):
    """Performs selection sort on a list of numbers.

    Args:
        numbers (list): A list of numbers to be sorted.

    Returns:
        list: The sorted list of numbers.

    Raises:
        TypeError: If input is not a list or contains non-numeric elements.
    """
    if not isinstance(numbers, list) or not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("Input must be a list of numbers.")

    for i in range(len(numbers)):
        min_idx = i
        for j in range(i+1, len(numbers)):
            if numbers[min_idx] > numbers[j]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    return numbers
def insertion_sort(numbers):
    """Performs insertion sort on a list of numbers.

    Args:
        numbers (list): A list of numbers to be sorted.

    Returns:
        list: The sorted list of numbers.

    Raises:
        TypeError: If input is not a list or contains non-numeric elements.
    """
    if not isinstance(numbers, list) or not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("Input must be a list of numbers.")

    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i-1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    return numbers
def quick_sort(numbers):
    """Performs quick sort on a list of numbers.

    Args:
        numbers (list): A list of numbers to be sorted.

    Returns:
        list: The sorted list of numbers.

    Raises:
        TypeError: If input is not a list or contains non-numeric elements.
    """
    if not isinstance(numbers, list) or not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("Input must be a list of numbers.")

    if len(numbers) <= 1:
        return numbers
    else:
        pivot = numbers[0]
        less = [x for x in numbers[1:] if x <= pivot]
        greater = [x for x in numbers[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
def sort_numbers(sort_type, numbers):
    """Sorts a list of numbers using the specified sorting algorithm.

    Args:
        sort_type (str): The name of the sorting algorithm to use ('bubble', 'selection', 'insertion', 'quick').
        numbers (list): A list of numbers to be sorted.

    Returns:
        list: The sorted list of numbers.

    Raises:
        ValueError: If the sort_type is not one of the supported algorithms.
    """
    sort_functions = {
        'bubble': bubble_sort,
        'selection': selection_sort,
        'insertion': insertion_sort,
        'quick': quick_sort
    }
    
    if sort_type not in sort_functions:
        raise ValueError("Unsupported sorting algorithm.")
    
    return sort_functions[sort_type](numbers)
class SortService:
    @cherrypy.expose
    def index(self, sort_type='bubble', numbers=""):
        """Handles HTTP GET requests to the index resource.

        Args:
            sort_type (str): The name of the sorting algorithm to use ('bubble', 'selection', 'insertion', 'quick').
            numbers (str): A comma-separated string of numbers to be sorted.

        Returns:
            A JSON response containing the sorted numbers.
        """
        try:
            numbers_list = [float(num) for num in numbers.split(',')]
            sorted_numbers = sort_numbers(sort_type, numbers_list)
            return {"sorted_numbers": sorted_numbers}
        except Exception as e:
            return {"error": str(e)}

if __name__ == '__main__':
    cherrypy.quickstart(SortService())
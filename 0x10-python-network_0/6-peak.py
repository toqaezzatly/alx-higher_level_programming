#!/usr/bin/python3
"""
Module to find a peak element in a list of unsorted integers.
"""

def find_peak(list_of_integers):
    """
    Finds a peak element in a list of unsorted integers.
    
    A peak element is an element that is greater than or equal to its neighbors.
    
    Args:
        list_of_integers (list): A list of unsorted integers.
    
    Returns:
        int: A peak element from the list, or None if the list is empty.
    """
    if not list_of_integers:
        return None

    def find_peak_util(arr, low, high, n):
        """
        Recursive helper function to find a peak element.
        
        Args:
            arr (list): The list of integers.
            low (int): The starting index of the current search range.
            high (int): The ending index of the current search range.
            n (int): The number of elements in the list.
        
        Returns:
            int: A peak element from the list.
        """
        mid = low + (high - low) // 2  # Calculate the middle index
        
        # Check if the middle element is a peak
        if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid]):
            return arr[mid]
        
        # If the left neighbor is greater, search the left half
        elif mid > 0 and arr[mid - 1] > arr[mid]:
            return find_peak_util(arr, low, mid - 1, n)
        
        # If the right neighbor is greater, search the right half
        else:
            return find_peak_util(arr, mid + 1, high, n)

    # Call the helper function with the initial parameters
    return find_peak_util(list_of_integers, 0, len(list_of_integers) - 1, len(list_of_integers))


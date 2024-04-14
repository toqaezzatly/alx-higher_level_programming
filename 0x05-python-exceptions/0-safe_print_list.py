#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print elements of a list up to a specified number.

    This function prints the elements of a given list up to a specified number,
    all on the same line followed by a new line.

    Args:
        my_list (list, optional): The list containing elements to be printed.
            Defaults to an empty list.
        x (int, optional): The number of elements to print. Defaults to 0.

    Returns:
        int: The real number of elements printed.

    Raises:
        None

    Example:
        >>> safe_print_list([1, 2, 3, 4, 5], 3)
        1 2 3
        3
        >>> safe_print_list(["apple", "banana", "orange"], 5)
        apple banana orange
        3

    Notes:
        - If x exceeds the length of my_list, it prints as many elements as possible.
        - If my_list is empty or x is 0, nothing will be printed.
    """
    try:
        printed_count = 0
        for i in range(x):
            print(my_list[i], end='')
            printed_count += 1
        print()  # Add a newline after printing elements
        return printed_count
    except IndexError:
        return printed_count


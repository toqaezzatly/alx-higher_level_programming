#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x integers from a list.

    Args:
        my_list (list): The list to print.
        x (int): The number of elements to access in my_list.

    Returns:
        int: The real number of integers printed.

    """
    try:
        printed_count = 0
        index = 0
        while printed_count < x:
            if isinstance(my_list[index], int):
                print("{:d}".format(my_list[index]), end='')
                printed_count += 1
            index += 1
        print()  # Add a newline after printing elements
        return printed_count
    except IndexError:
        return printed_count

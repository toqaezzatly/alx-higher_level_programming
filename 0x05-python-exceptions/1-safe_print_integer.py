#!/usr/bin/python3
def safe_print_integer(value):
    """Prints an integer with "{:d}".format().

    Args:
        value: The value to print.

    Returns:
        bool: True if value has been correctly printed (it means the value is an integer),
              False otherwise.
    """
    try:
        if value is None or not isinstance(value, int):
            return False
        print("{:d}".format(value))
        return True
    except ValueError:
        print("False")
        return False


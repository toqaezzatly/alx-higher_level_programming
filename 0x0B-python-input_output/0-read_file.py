#!/usr/bin/python3
def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

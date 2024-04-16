#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns the number of characters added.
    If the file doesn't exist, it will be created.
    """
    try:
        with open(filename, "a", encoding="utf-8") as file:
            num_chars_added = file.write(text)
            return num_chars_added
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0


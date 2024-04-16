#!/usr/bin/python3
"""
A function writes an obj to a text file
using JSON file
"""
def save_to_json(my_obj, filename):
    """
    This fuction writes json to text file.
    Args: my_obj: string, filename: string.
    """
    with open(filename, 'w', encoding="utf-8") as file_opened:
        file_opened.write(json.dumps(my_obj))

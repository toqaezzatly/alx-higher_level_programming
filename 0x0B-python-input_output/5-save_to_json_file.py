#!/usr/bin/python3
import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(my_obj, file, ensure_ascii=False, indent=4)
        return f"Object saved to {filename}"
    except Exception as e:
        return f"An error occurred: {e}"

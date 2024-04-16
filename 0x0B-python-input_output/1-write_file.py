#!/usr/bin/python3
def write_file(filename="", text=""):
    '''
    writes a string to a file (UTF8)
    and retuens the number of characters written.
    if the file exists, it overwrites the content;
    otherwis it creats a new file.
    '''
    try:
        with open(filename, "w", encoding="utf-8") as file:
            num_char_written = file.write(text)
            return num_char_written
    except Exception as e:
        print(f"An error occured: {e}")
        return 0

#!/usr/bin/node

import sys

def write_to_file(file_path, content):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print("Content successfully written to the file.")
    except Exception as e:
        print("An error occurred while writing to the file:", e)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <file_path> <content>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    content = sys.argv[2]
    
    write_to_file(file_path, content)

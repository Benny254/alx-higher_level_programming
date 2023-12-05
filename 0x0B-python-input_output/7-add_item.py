#!/usr/bin/python3

import sys
from os.path import isfile
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def add_item_to_list_and_save(args):
    """Add command line arguments to a list and save to add_item.json."""
    file_name = 'add_item.json'

    # Load existing data from the file or create an empty list
    items_list = load_from_json_file(file_name) if isfile(file_name) else []

    # Add new items from command line arguments to the list
    items_list.extend(args)

    # Save the updated list to the file
    save_to_json_file(items_list, file_name)

if __name__ == "__main__":
    # Exclude the script name itself from the arguments
    arguments = sys.argv[1:]

    if not arguments:
        print("Usage: ./add_item.py <item1> <item2> ...")
        sys.exit(1)

    add_item_to_list_and_save(arguments)


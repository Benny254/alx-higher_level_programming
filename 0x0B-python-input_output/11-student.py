#!/usr/bin/python3
class Student:
    # ... (existing code)

    def reload_from_json(self, json):
        # Get an iterator for the items in the dictionary
        iterator = iter(json.items())

        # Use a while loop to iterate over the items
        while True:
            try:
                # Get the next key-value pair
                k, v = next(iterator)

                # Set the attribute on the object
                setattr(self, k, v)
            except StopIteration:
                # Break the loop when there are no more items
                break

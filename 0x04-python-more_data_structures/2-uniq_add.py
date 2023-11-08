def uniq_add(my_list=[]):
    """Add all unique integers in a list."""
    result = 0
    for t in set(my_list):
        if isinstance(t, int):
            result += t
    return result
   

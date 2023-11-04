def add_tuple(tuple_a=(), tuple_b=()):
    # Pad tuples with zeros if they have less than 2 elements
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    # Take only the first 2 elements of each tuple
    sum_first_element = tuple_a[0] + tuple_b[0]
    sum_second_element = tuple_a[1] + tuple_b[1]

    return (sum_first_element, sum_second_element)

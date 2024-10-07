def tuple_operations():
    """Performs various operations on tuples."""

    numbers = (1, 2, 3, 4, 5)

    print("Original tuple:", numbers)

    # Tuple functions
    print("Tuple functions:")

    # Accessing elements
    print("First element:", numbers[0])
    print("Last element:", numbers[-1])

    # Slicing
    sliced_tuple = numbers[1:3]
    print("Sliced tuple:", sliced_tuple)

    # Concatenation
    new_tuple = numbers + (6, 7, 8)
    print("Concatenated tuple:", new_tuple)

    # Index
    index = numbers.index(3)
    print("Index of 3:", index)

    # Count
    count = numbers.count(3)
    print("Count of 3:", count)

    # Len
    length = len(numbers)
    print("Length of tuple:", length)

    # Tuple to list
    list_from_tuple = list(numbers)
    print("List from tuple:", list_from_tuple)

    # List to tuple
    tuple_from_list = tuple(list_from_tuple)
    print("Tuple from list:", tuple_from_list)

    # Unpacking
    a, b, c, d, e = numbers
    print("Unpacked values:", a, b, c, d, e)

    # Packing
    packed_tuple = (a, b, c, d, e)
    print("Packed tuple:", packed_tuple)

    # Equality
    equality = numbers == packed_tuple
    print("Equality:", equality)

    # Inequality
    inequality = numbers != packed_tuple
    print("Inequality:", inequality)

    # Greater than
    greater_than = numbers > packed_tuple
    print("Greater than:", greater_than)

    # Less than
    less_than = numbers < packed_tuple
    print("Less than:", less_than)

    # Greater than or equal to
    greater_than_or_equal_to = numbers >= packed_tuple
    print("Greater than or equal to:", greater_than_or_equal_to)

    # Less than or equal to
    less_than_or_equal_to = numbers <= packed_tuple
    print("Less than or equal to:", less_than_or_equal_to)

tuple_operations()


import array

def array_operations():
    """Performs various operations on arrays."""

    numbers = array.array('i', [1, 2, 3, 4, 5])

    print("Original array:", numbers)

    # Array functions
    print("Array functions:")

    # Accessing elements
    print("First element:", numbers[0])
    print("Last element:", numbers[-1])

    # Slicing
    sliced_array = numbers[1:3]
    print("Sliced array:", sliced_array)

    # Append
    numbers.append(6)
    print("Array after appending:", numbers)

    # Extend
    numbers.extend(array.array('i', [7, 8, 9]))
    print("Array after extending:", numbers)

    # Insert
    numbers.insert(2, 10)
    print("Array after inserting:", numbers)

    # Remove
    numbers.remove(10)
    print("Array after removing:", numbers)

    # Pop
    popped_element = numbers.pop(2)
    print("Popped element:", popped_element)
    print("Array after popping:", numbers)

    # Index
    index = numbers.index(5)
    print("Index of 5:", index)

    # Count
    count = numbers.count(5)
    print("Count of 5:", count)

    # Tolist
    list_from_array = numbers.tolist()
    print("List from array:", list_from_array)

    # Totypecode
    typecode = numbers.typecode
    print("Typecode:", typecode)

    # Itemsize
    itemsize = numbers.itemsize
    print("Itemsize:", itemsize)

    # Byteswap
    numbers.byteswap()
    print("Array after byteswapping:", numbers)

    # Frombytes
    bytes_array = array.array('i')
    bytes_array.frombytes(b'\x00\x00\x00\x01\x00\x00\x00\x02')
    print("Array from bytes:", bytes_array)

    # Tobytes
    bytes_from_array = numbers.tobytes()
    print("Bytes from array:", bytes_from_array)

array_operations()
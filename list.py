def list_operations():
    """Performs various operations on lists."""

    numbers = [1, 2, 3, 4, 5]

    print("Original list:", numbers)

    # List functions
    print("List functions:")

    # Accessing elements
    print("First element:", numbers[0])
    print("Last element:", numbers[-1])

    # Slicing
    sliced_list = numbers[1:3]
    print("Sliced list:", sliced_list)

    # Concatenation
    new_list = numbers + [6, 7, 8]
    print("Concatenated list:", new_list)

    # Append
    numbers.append(9)
    print("List after appending:", numbers)

    # Extend
    numbers.extend([10, 11, 12])
    print("List after extending:", numbers)

    # Insert
    numbers.insert(2, 13)
    print("List after inserting:", numbers)

    # Remove
    numbers.remove(13)
    print("List after removing:", numbers)

    # Pop
    popped_element = numbers.pop(2)
    print("Popped element:", popped_element)
    print("List after popping:", numbers)

    # Index
    index = numbers.index(5)
    print("Index of 5:", index)

    # Count
    count = numbers.count(5)
    print("Count of 5:", count)

    # Sort
    numbers.sort()
    print("Sorted list:", numbers)

    # Reverse
    numbers.reverse()
    print("Reversed list:", numbers)

    # Copy
    copied_list = numbers.copy()
    print("Copied list:", copied_list)

    # Clear
    numbers.clear()
    print("List after clearing:", numbers)

    # List comprehension
    squares = [x**2 for x in range(10)]
    print("Squares of numbers from 0 to 9:", squares)

    # Map
    numbers = [1, 2, 3, 4, 5]
    doubled_numbers = list(map(lambda x: x*2, numbers))
    print("Doubled numbers:", doubled_numbers)

    # Filter
    even_numbers = list(filter(lambda x: x%2 == 0, numbers))
    print("Even numbers:", even_numbers)

    # Reduce
    from functools import reduce
    product = reduce(lambda x, y: x*y, numbers)
    print("Product of numbers:", product)

    # Zip
    numbers1 = [1, 2, 3]
    numbers2 = [4, 5, 6]
    zipped_list = list(zip(numbers1, numbers2))
    print("Zipped list:", zipped_list)

    # Unzip
    unzipped_list1, unzipped_list2 = zip(*zipped_list)
    print("Unzipped list 1:", unzipped_list1)
    print("Unzipped list 2:", unzipped_list2)

    # Enumerate
    for index, value in enumerate(numbers):
        print("Index:", index, "Value:", value)

    # Any
    any_true = any(numbers)
    print("Any true:", any_true)

    # All
    all_true = all(numbers)
    print("All true:", all_true)

    # Sum
    sum_of_numbers = sum(numbers)
    print("Sum of numbers:", sum_of_numbers)

    # Max
    max_number = max(numbers)
    print("Max number:", max_number)

    # Min
    min_number = min(numbers)
    print("Min number:", min_number)

list_operations()
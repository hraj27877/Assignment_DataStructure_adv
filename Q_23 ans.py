# Write a code to concatenate two tuples. The function should take two tuples as input and return a new tuple containing elements from both input tuples


def concatenate_tuples(tuple1, tuple2):
    # Concatenate the two tuples
    result = tuple1 + tuple2
    return result

# Example usage
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = concatenate_tuples(tuple1, tuple2)
print(result)

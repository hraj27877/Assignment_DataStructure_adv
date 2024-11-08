# Write a code that takes two tuples as input and returns a new tuple containing elements that are common to both input tuples


def common_elements(tuple1, tuple2):
    # Convert tuples to sets and find the intersection
    set1 = set(tuple1)
    set2 = set(tuple2)
    
    # Find the intersection and convert it back to a tuple
    common = tuple(set1 & set2)
    
    return common

# Example usage
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7)
result = common_elements(tuple1, tuple2)
print(result)

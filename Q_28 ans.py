#  Create a code that defines two sets of integers. Then, print the union, intersection, and difference of these two sets


def main():
    # Define two sets of integers
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    
    # Calculate the union of the two sets
    union = set1 | set2
    # Calculate the intersection of the two sets
    intersection = set1 & set2
    # Calculate the difference of set1 and set2 (elements in set1 but not in set2)
    difference = set1 - set2
    
    # Print the results
    print("Union of the two sets:", union)
    print("Intersection of the two sets:", intersection)
    print("Difference of set1 and set2:", difference)

# Call the main function
main()

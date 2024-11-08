# Create a code to check if a given list is sorted (either in ascending or descending order) or not


def is_sorted(lst):
    # Check if list is sorted in ascending order
    ascending = all(lst[i] <= lst[i+1] for i in range(len(lst) - 1))
    
    # Check if list is sorted in descending order
    descending = all(lst[i] >= lst[i+1] for i in range(len(lst) - 1))
    
    # Return True if the list is sorted in either order, False otherwise
    return ascending or descending

# Example usage
lst = [1, 2, 3, 4, 5]
result = is_sorted(lst)
print(f"Is the list sorted? {result}")

lst2 = [5, 4, 3, 2, 1]
result2 = is_sorted(lst2)
print(f"Is the list sorted? {result2}")

lst3 = [1, 3, 2, 4]
result3 = is_sorted(lst3)
print(f"Is the list sorted? {result3}")

# Write a code to reverse a list in-place without using any built-in reverse functions


def reverse_list_in_place(lst):
    left, right = 0, len(lst) - 1  # Initialize pointers to the start and end of the list
    while left < right:
        # Swap elements at left and right
        lst[left], lst[right] = lst[right], lst[left]
        left += 1  # Move the left pointer to the right
        right -= 1  # Move the right pointer to the left
    return lst

# Example usage
lst = [1, 2, 3, 4, 5]
result = reverse_list_in_place(lst)
print(result)

# Implement a code to find the second largest number in a given list of integers

def find_second_largest(nums):
    if len(nums) < 2:
        return None  # Return None if there are fewer than 2 elements
    
    first, second = float('-inf'), float('-inf')  # Initialize variables to hold the largest and second largest numbers

    for num in nums:
        if num > first:
            second = first  # Update second largest
            first = num  # Update largest
        elif num > second and num != first:
            second = num  # Update second largest if it's smaller than first but larger than second
    
    return second if second != float('-inf') else None  # If no second largest, return None

# Example usage
nums = [12, 35, 1, 10, 34, 1]
result = find_second_largest(nums)
print(f"The second largest number is: {result}")

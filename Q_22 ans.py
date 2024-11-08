# Create a code that prompts the user to enter two sets of integers separated by commas. Then, print the intersection of these two sets


def main():
    # Prompt the user to enter two sets of integers
    set1_input = input("Enter the first set of integers, separated by commas: ")
    set2_input = input("Enter the second set of integers, separated by commas: ")
    
    # Convert the input strings into sets of integers
    set1 = set(map(int, set1_input.split(',')))
    set2 = set(map(int, set2_input.split(',')))
    
    # Find the intersection of the two sets
    intersection = set1 & set2
    
    # Print the intersection
    print("The intersection of the two sets is:", intersection)

# Call the main function
main()

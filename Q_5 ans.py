#Write a code to find all occurrences of a given substring within another string

def find_occurrences(main_string, substring):
    occurrences = []
    start = 0

    while True:
        # Find the next occurrence of the substring
        index = main_string.find(substring, start)
        
        # If no more occurrences are found, break the loop
        if index == -1:
            break
        
        # Add the index to the list of occurrences
        occurrences.append(index)
        
        # Move the start position to the next character after the found occurrence
        start = index + 1

    return occurrences

# Test the function
main_string = "This is a test string and this is just a test."
substring = "is"
positions = find_occurrences(main_string, substring)
print("Occurrences of substring found at positions:", positions)

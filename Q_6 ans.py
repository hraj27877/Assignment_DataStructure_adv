# Write a code to determine if a string has all unique characters

def has_unique_characters(s):
    # Use a set to track characters we've seen
    seen_characters = set()

    # Loop through each character in the string
    for char in s:
        # If the character is already in the set, it's not unique
        if char in seen_characters:
            return False
        # Otherwise, add the character to the set
        seen_characters.add(char)

    # If we complete the loop without finding duplicates, all characters are unique
    return True

# Test the function
string = "abcdefg"
if has_unique_characters(string):
    print("The string has all unique characters.")
else:
    print("The string does not have all unique characters.")

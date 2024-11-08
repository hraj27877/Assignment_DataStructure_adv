#Write a code to check if a given string is a palindrome or not.

def is_palindrome(string):
    # Convert the string to lowercase and remove spaces
    cleaned_string = string.replace(" ", "").lower()
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

# Test the function
string = "A man a plan a canal Panama"
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

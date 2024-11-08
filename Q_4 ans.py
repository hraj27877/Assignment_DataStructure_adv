# Write a code to check if two given strings are anagrams of each other

def are_anagrams(string1, string2):
    # Remove spaces, convert to lowercase, and sort both strings
    cleaned_string1 = ''.join(sorted(string1.replace(" ", "").lower()))
    cleaned_string2 = ''.join(sorted(string2.replace(" ", "").lower()))
    
    # Check if the sorted versions of both strings are the same
    return cleaned_string1 == cleaned_string2

# Test the function
string1 = "listen"
string2 = "silent"
if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

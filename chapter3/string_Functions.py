name = "Harry"

print(len(name))
print(name.endswith("arry"))  #true
print(name.startswith("Har"))  # true
print(name.startswith("har"))  # falses
print(name.capitalize()) #makes the first letter capital

# Sample string
s = "   Hello, World!   "  # Contains leading and trailing spaces
words = ["Python", "is", "awesome"]  # List of words for join example

# len()
print("Length of string:", len(s))  
# Explanation: Counts the total characters including spaces. Output: 18

# lower()
print("Lowercase:", s.lower())  
# Explanation: Converts all characters to lowercase. Output: "   hello, world!   "

# upper()
print("Uppercase:", s.upper())  
# Explanation: Converts all characters to uppercase. Output: "   HELLO, WORLD!   "

# strip()
print("Stripped:", s.strip())  
# Explanation: Removes leading and trailing whitespace. Output: "Hello, World!"

# split()
print("Split:", s.split())  
# Explanation: Splits the string into a list using spaces as default delimiters. Output: ['Hello,', 'World!']

# join()
print("Joined:", " ".join(words))  
# Explanation: Joins the list elements into a single string with spaces between them. Output: "Python is awesome"

# replace()
print("Replace 'World' with 'Python':", s.replace("World", "Python"))  
# Explanation: Replaces occurrences of "World" with "Python". Output: "   Hello, Python!   "

# find()
print("Find 'World':", s.find("World"))  
# Explanation: Returns the index where "World" starts. Output: 10

# startswith()
print("Starts with 'Hello':", s.startswith("Hello"))  
# Explanation: Checks if the string starts with "Hello". Output: False (because of leading spaces)

# endswith()
print("Ends with '!':", s.endswith("!"))  
# Explanation: Checks if the string ends with "!". Output: True (ignores trailing spaces)

# isalpha()
alpha_string = "Hello"
print(f"Is '{alpha_string}' alphabetic?:", alpha_string.isalpha())  
# Explanation: Returns True if all characters are alphabets. Output: True

# isdigit()
digit_string = "12345"
print(f"Is '{digit_string}' numeric?:", digit_string.isdigit())  
# Explanation: Returns True if all characters are digits. Output: True

# islower() / isupper()
lowercase_string = "hello"
uppercase_string = "HELLO"
print(f"Is '{lowercase_string}' all lowercase?:", lowercase_string.islower())  
# Explanation: Checks if all characters are lowercase. Output: True
print(f"Is '{uppercase_string}' all uppercase?:", uppercase_string.isupper())  
# Explanation: Checks if all characters are uppercase. Output: True

# capitalize()
print("Capitalize:", s.capitalize())  
# Explanation: Capitalizes the first character of the string. Output: "   hello, world!   "

# title()
print("Title case:", s.title())  
# Explanation: Converts the first character of each word to uppercase. Output: "   Hello, World!   "

# Input two strings
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Concatenate strings and store in another variable
result = str1 + " " + str2

print("\nConcatenated String:", result)

# Performing string methods
print("\n--- String Methods Output ---")

print("lower()      :", result.lower())
print("upper()      :", result.upper())
print("title()      :", result.title())
print("swapcase()   :", result.swapcase())
print("capitalize() :", result.capitalize())
print("casefold()   :", result.casefold())

print("center(50)   :", result.center(50, "*"))

# count()
word = input("\nEnter word/character to count: ")
print("count()      :", result.count(word))

# endswith()
suffix = input("Enter suffix to check: ")
print("endswith()   :", result.endswith(suffix))

# find()
find_word = input("Enter word to find: ")
print("find()       :", result.find(find_word))

# Checking methods
print("isalnum()    :", result.isalnum())
print("isdigit()    :", result.isdigit())
print("isnumeric()  :", result.isnumeric())
print("isspace()    :", result.isspace())

# replace()
old_word = input("\nEnter word to replace: ")
new_word = input("Enter new word: ")
print("replace()    :", result.replace(old_word, new_word))
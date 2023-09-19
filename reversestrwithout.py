#reverse a string without built in functions
strings=input("Enter your string: ")
revStrings=""
for char in strings:
    revStrings=char+revStrings
print("Reverse string is: ",revStrings)
#find the string is palindrom or not without built in functions
strings=input("Enter your string: ")
revStrings=""
for char in strings:
    revStrings=char+revStrings
print("Reverse string is: ",revStrings)
if(strings==revStrings):
    print("String is Pallindrom")
else:
    print("String is not Pallindrom")


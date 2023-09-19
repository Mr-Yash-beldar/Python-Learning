import arithmatic as solve
num=int(input("Enter number: "))
armStrong=solve.armstrongNumber(num)
if(armStrong):
    print("it's Armstrong ")
else:
    print("it's not Armstrong ")

# factorial=solve.factorial(num)
# print(f"factorial of {num} is {factorial}")

reverseNumber=solve.reverseNumber(num)
print(f"Reverse number of {num} is {reverseNumber}")

palindrome=solve.palindrome(num)
if(palindrome):
    print(f"{num} is palindrome number")
else:
    print(f"{num} is not palindrome number")
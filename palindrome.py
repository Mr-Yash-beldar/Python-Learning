# Check number is palindrome or not
num=int(input("Number: "))
n=num
rev=0
while(num>0):
    rem=num%10;
    rev=(rev*10)+rem;
    num=num//10;
if(rev==n):
    print(f"{n} is palindrome number")
else:
    print(f"{n} is not palindrome number")

# Number of digits in number
num=int(input("Number: "))
sum=0;
while(num>0):
    rem=num%10;
    sum=sum+1
    num=num//10;
print("Digit: ",sum)
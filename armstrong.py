# 
# Armstrong Number
num=int(input("Number: "))
n=num
sum=0;
while(num>0):
    rem=num%10;
    sum=sum+(rem**3)
    num=num//10;
if(sum==n):
    print(f"{n} is Armstrong Number")
else:
    print(f"{n} is not Armstrong Number")
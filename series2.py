def fact(num)-> int:  
    fact=1;
    for i in range (1,num+1):
        fact=fact*i
    return fact
x=2
n=5
sum=1
for i in range(1,n+1):
    sum=sum+(pow(x, i)/fact(i))
print(sum)
#ZeroDivisionError
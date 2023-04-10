# Sum of all odd in range

num=int(input("Number: "))
sum=0
for i in range (1,num+1):
    if(i%2==1):
        sum=sum+i
print(sum)

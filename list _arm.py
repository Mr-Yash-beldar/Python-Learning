def arm(n) -> int:
     n = i
     sum=0;
     while(i>0):
        rem=i%10;
        sum=sum+(rem**3)
        i=i//10;
     if(sum==n):
        return sum
    
# List Of Armstrong
num=[123,153,12,4,371]
list=[]
for j in num:
        list.append(arm(j))
print(num)
print(list)


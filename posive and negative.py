nums=[12,-5,-45,-8,3,7]
sumneg=0
sumpos=0
for i in nums:
    if(i<=0):
        sumneg=sumneg+i
    else:
        sumpos=sumpos+i
print("Negative numbers sum: ",sumneg)
print("Positive numbers sum: ",sumpos)
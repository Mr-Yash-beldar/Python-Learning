def euclid(a,b)->int:
    if(b==0):
        return a
    else:
        return euclid(b,(a%b))
    
a=int(input("Enter First numbers: "))
b=int(input("Enter Second numbers: "))

print("Euclid: ",euclid(a,b))
a=int(input("1st"))
b=int(input("2ed"))
c=int(input("3rd"))
print((a > b and b > c) and a or (b > a and a > c) and b or c)
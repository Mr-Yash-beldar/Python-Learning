def arithmatic(a,b):
    add=a+b
    mul=a*b
    sub=a-b
    div=a/b
    return add,mul,sub,div
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
add,mul,sub,div=arithmatic(a,b)
print(add)
print(mul)
print(sub)
print(div)

def findPeri(a, b):
    p = 2*(a+b)
    return p

def findArea(a,b):
    area = a*b
    return area
print("Enter Length and Breadth of Rectangle: ", end="")
l = float(input())
b = float(input())

res = findPeri(l, b)
print("\nPerimeter = {:.2f}".format(res))

area = findArea(l, b)
print("\nArea = {:.2f}".format(area))
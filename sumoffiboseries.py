# Python program to find Fibonacci series sum up to n
num = 5
sum=0
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
sum=sum+n1+n2
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")
    sum=sum+n3

print("\nsum of series is: ",sum)
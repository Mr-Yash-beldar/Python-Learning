def reverseNumber(num) -> int:
    rev = 0
    while (num > 0):
        rem = num % 10
        rev = (rev*10)+rem
        num = num//10
    return rev


def armstrongNumber(num) -> bool:
    n = num
    
    sum = 0
    while (num > 0):
        rem = num % 10
        sum = sum+(rem**(3))
        num = num//10
    if (sum == n):
        return True
    else:
        return False


def factorial(num) -> int:
    fact = 1
    for i in range(1, num+1):
        fact = fact*i
    return fact


def palindrome(num) -> bool:
    n = num
    rev = 0
    while (num > 0):
        rem = num % 10
        rev = (rev*10)+rem
        num = num//10
    if (rev == n):
        return True
    else:
        return False

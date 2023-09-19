numbers=[2,3,4,5,4]
def sumoflist(numbers):
    if not numbers:
        return 0
    else:
        return numbers[0]+sumoflist(numbers[1:])

nums=[2,3,4,5,4]   
print(sumoflist(nums))
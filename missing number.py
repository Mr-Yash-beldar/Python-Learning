def missing_number(nums):
    n = len(nums) + 1  
    total_sum = (n * (n + 1)) // 2 
    list_sum = sum(nums)  
    missing_number = total_sum - list_sum
    return missing_number


nums = [1, 2,4,3, 5,6]  
missing_number = missing_number(nums)
print("Missing number is :", missing_number)

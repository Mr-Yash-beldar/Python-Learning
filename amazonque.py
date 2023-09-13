nums = [1, 3, 2, 4]
ans = []
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if (nums[i] < nums[j]):
            ans.append(nums[j])
            break
ans.append(-1)
print(ans)

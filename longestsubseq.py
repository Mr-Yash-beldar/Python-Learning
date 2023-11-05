def longest_subsequence(arr):  
    arr = list(set(arr))  # Remove duplicates
    arr.sort()            # Sort the array

    longest_seq = []
    current_seq = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1] + 1:
            current_seq.append(arr[i])
        else:
            if len(current_seq) > len(longest_seq):
                longest_seq = current_seq[:]
            current_seq = [arr[i]]

    if len(current_seq) > len(longest_seq):
        longest_seq = current_seq

    return longest_seq

# Example usage:
arr = [100, 4, 200, 1, 3, 2]
result = longest_subsequence(arr)
print("Longest Consecutive Subsequence:", result)

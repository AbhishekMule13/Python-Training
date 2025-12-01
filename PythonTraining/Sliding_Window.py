def longestBalancedSubarray(nums):
    
    balance = 0
    first_time_seen = {0: -1}
    longest = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            balance += 1
        else:
            balance -= 1

        if balance in first_time_seen:
            current_length = i - first_time_seen[balance]
            longest = max(longest, current_length)
        else:
            first_time_seen[balance] = i

            

    return longest

nums = [0, 1, 0, 0, 1, 1]
print(longestBalancedSubarray(nums))
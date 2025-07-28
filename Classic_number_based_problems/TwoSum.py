class Solutions(object):
    def TwoSum(self, nums, target):
        n=len(nums)
        for i in range (n):
            for j in range (i+1, n):
                if nums[i]+nums[j]==target:
                    return [i , j]
nums=[2,3,4,5,6,9,7,8,0] 
target=11    

s=Solutions()
print(s.TwoSum(nums , target))
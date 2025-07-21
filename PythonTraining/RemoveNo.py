class Solution(object):
    def removeElement(self, nums, val):
        k=0
        for i in range (len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        return k
nums=[2,3,4,2,4,2,2,5,2,4,2,6,2,4,2]  
val=2

sol = Solution()
k = sol.removeElement(nums, val)

# Output
print("k =", k)
print("Modified nums =", nums[:k])

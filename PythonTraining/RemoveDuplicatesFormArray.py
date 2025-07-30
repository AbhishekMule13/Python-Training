class solutions(object):
    def RemoveDuplicates(self,nums):
        if not nums:
            return 0
        i=0
        for j in range(1, len(nums)):
            if nums[j]!=nums[i]:
               i+=1
               nums[i]=nums[j]
        return i+1
nums=list(map(int, input("enter the numbers:").split()))
s=solutions() 
length = s.RemoveDuplicates(nums)
print("After Removing Duplicates:",nums[:length])
#print(nums[:length])       
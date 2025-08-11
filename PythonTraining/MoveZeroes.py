while True:
    class solution(object):
        def MoveZeroes(self, nums):
            pointer=0
            for i in range(len(nums)):
                if nums[i]!=0:
                    nums[pointer], nums[i] = nums[i], nums[pointer]
                    pointer+=1
    nums=list(map(int, input("Enter the numbers:").split()))
    solution().MoveZeroes(nums)
    print(nums)                
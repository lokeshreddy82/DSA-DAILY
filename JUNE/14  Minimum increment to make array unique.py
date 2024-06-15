class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res=0
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                nums[i]=nums[i]+1
                res +=1
            elif nums[i-1]>nums[i]:
                res +=(nums[i-1]-nums[i])
                nums[i]=nums[i]+nums[i-1]-nums[i]+1
                res +=1
        return res

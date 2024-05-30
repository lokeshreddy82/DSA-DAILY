class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        nums.sort()
        i=0
        j=len(nums)-1
        while i<j:
            if nums[i]>0:
                return -1
            elif nums[i]==-1*nums[j]:
                return nums[j]
            elif -1*nums[i]<nums[j]:
                j -=1
            else:
                i +=1
        return -1
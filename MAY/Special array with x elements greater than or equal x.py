import bisect
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n=len(nums)
        res=-1
        nums.sort()
        for i in range(1,n+1):
            l=bisect.bisect_left(nums,i)
            if l==n:
                break
            if (i<nums[l] or i==nums[l]) and i==len(nums[l:]):
                res=len(nums[l:])
                break
        return res
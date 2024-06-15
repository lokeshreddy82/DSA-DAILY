class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<3:
            nums.sort()
        else:
            p1,p2,p3=0,0,len((nums))-1
            while p2<=p3:
                if nums[p2]==0:
                    nums[p2],nums[p1]=nums[p1],nums[p2]
                    p1 +=1
                    p2 +=1
                elif nums[p2]==1:
                    p2 +=1
                else:
                    nums[p3],nums[p2]=nums[p2],nums[p3]
                    p3 -=1

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res=0
        n=len(nums)
        def dfs(ind,prev):
            if ind==n:
                nonlocal res
                res +=prev
                return
            dfs(ind+1,prev^nums[ind])
            dfs(ind+1,prev)
        dfs(0,0)
        return res
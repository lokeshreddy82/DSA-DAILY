class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        self.res=0
        n=len(nums)
        ans=[]
        def isSafe(ds:List[int],element:int)->bool:
            for i in ds:
                if abs(i-element)==k:
                    return False
            return True
        def dfs(ind:int,ds:List[int])->None:
            if ind==n:
                if ds:
                    ans.append(ds[:])
                    self.res +=1
                return
            if isSafe(ds,nums[ind]):
                dfs(ind+1,ds+[nums[ind]])
            dfs(ind+1,ds)
        dfs(0,[])
        return self.res
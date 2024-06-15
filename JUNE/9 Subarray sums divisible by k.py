class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res=0
        hashing={0:1}
        prefix=0
        for i in range(len(nums)):
            prefix +=nums[i]
            p=(prefix-k)%k
            if p<0:
                p +=k
            res +=hashing.get(p,0)
            hashing[p]=hashing.get(p,0)+1
        return res

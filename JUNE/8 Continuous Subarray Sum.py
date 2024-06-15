class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen, prefix = {0: -1}, 0
        for i, num in enumerate(nums):
            prefix = (prefix + num) % k
            if prefix in seen:
                if i - seen[prefix] > 1:
                    return True
            else:
                seen[prefix] = i
        return False

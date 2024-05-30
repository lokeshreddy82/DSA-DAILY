class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        s = 0
        val = 0
        for i in range(k):
            s += max(0, happiness[i]-val)
            val += 1    
        return s
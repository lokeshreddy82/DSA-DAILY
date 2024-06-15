from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n=len(arr2)
        res=[]
        hashing=Counter(arr1)
        for i in range(n):
            c=hashing[arr2[i]]
            e=arr2[i]
            res = res +[e for i in range(c)]
            del hashing[e]
        extra=[]
        for key,value in hashing.items():
            extra=extra+[key for i in range(value)]
        return res+sorted(extra)

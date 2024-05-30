import heapq
class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> List[int]:
        ar=[]
        n=len(arr)
        for i in range(n-1):
            for j in range(i+1,n):
                ar.append((arr[i]/arr[j],arr[i],arr[j]))
        heapq.heapify(ar)
        res=heapq.nsmallest(k,ar)[-1]
        return [res[1],res[2]]
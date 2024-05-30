class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n=len(score)
        if len(score)<3:
            if len(score)==1:
                return ["Gold Medal"]
            else:
                l=["Gold Medal","Silver Medal"]
                if score[0]>score[1]:
                    return l
                else:
                    l[0],l[1]=l[1],l[0]
                    return l
        copyy=score.copy()
        copyy.sort(reverse=True)
        indexes={}
        for i in range(len(score)):
            indexes[copyy[i]]=i
        res=[]
        hashing={
        1:"Gold Medal",
        2:"Silver Medal",
        3:"Bronze Medal"
        }
        for i in score:
            ind=indexes[i]
            if ind+1 in hashing:
                res.append(hashing.get(ind+1))
            else:
                res.append(str(ind+1))
        return res
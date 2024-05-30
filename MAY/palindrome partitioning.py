class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n=len(s)
        res=[]
        m=n+1
        def dfs(prev:int,ind:int,ds:list[str])->None:
            if ind==m:
                res.append(ds[:])
                return
            for i in range(ind,n+1):
                if s[prev:i]==s[prev:i][::-1]:
                    dfs(i,i+1,ds+[s[prev:i]])
            return
        dfs(0,1,[])
        return res
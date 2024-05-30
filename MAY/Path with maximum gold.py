class Solution:
    def ischeck(self,row:int,col:int):
        if row<self.m and row>=0 and col>=0 and  self.n>col:
            return True
        return False
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.m=len(grid)
        self.n=len(grid[0])
        vis=[[True for i in range(self.n)] for j in range(self.m)]
        dir=[(0,-1),(-1,0),(0,1),(1,0)]
        def dfs(i:int,j:int,vis:List[List[bool]],ans)->int:
            vis[i][j]=False
            k=0
            for r,c in dir:
                
                r=r+i
                c=c+j
                if self.ischeck(r,c) and grid[r][c]!=0 and vis[r][c]:
                    k=max(k,dfs(r,c,vis,ans+grid[r][c]))
            ans=max(ans,k)
            vis[i][j]=True
            return ans
        res=0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j]!=0:
                    res=max(res,dfs(i,j,vis,grid[i][j]))
        return res
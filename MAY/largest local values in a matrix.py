class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n=len(grid)
        k=n-2
        res=[[1 for i in range(n-2)] for j in range(n-2)]
        self.l=0
        self.r=0
        end=n-2
        def dfs(strw,endr,stc,endc):
            maxi=0
            for i in range(strw,endr+1):
                for j in range(stc,endc+1):
                    maxi=max(maxi,grid[i][j])
            if self.r==end:
                self.l +=1
                self.r=0
            res[self.l][self.r]=maxi
            self.r +=1
        for i in range(1,n-1):
            for j in range(1,n-1):
                dfs(i-1,i+1,j-1,j+1)
        return res
                
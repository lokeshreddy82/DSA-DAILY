class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        def conversion(i,j,row):
            if row:
                for j in range(n):
                    if grid[i][j]==1:
                        grid[i][j]=0
                    else:
                        grid[i][j]=1
            else:
                for i in range(m):
                    if grid[i][j]==1:
                        grid[i][j]=0
                    else:
                        grid[i][j]=1
        res=0
        for i in range(m):
            if grid[i][0]==0:
                conversion(i,0,True)
        def countt(i,j):
            zero,one=0,0
            for i in range(m):
                if grid[i][j]==0:
                    zero +=1
                else:
                    one +=1
            return (zero,one)
        i=0
        for j in range(1,n):
            i +=1
            zero_countt,one_countt=countt(i,j)
            if zero_countt>one_countt:
                conversion(i,j,False)
        for i in range(m):
            s=""
            for j in range(n):
                s +=str(grid[i][j])
            res +=int(s,2)
        return res
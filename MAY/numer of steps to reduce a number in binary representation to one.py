class Solution:
    #it is brute force i know it will execute because of constrains
    #and it is not optimal use construct algorithm technique or gready
    
    def numSteps(self, s: str) -> int:
        r=0
        s=int(s,2)
        while s!=1:
            r +=1
            if s%2==0:
                s=s>>1
            else:
                s +=1
        return r
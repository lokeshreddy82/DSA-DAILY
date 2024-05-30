class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        boats=0
        boatlist=[]
        l,r=0,len(people)-1
        people.sort()
        while l<=r:
            if people[l]+people[r]<=limit:
                boatlist.append([people[l],people[r]])
                l+=1
                r-=1
            else:
                boatlist.append([people[r]])
                r-=1

            boats+=1
        print(boatlist)
        return boats


            
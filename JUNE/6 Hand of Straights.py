class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n=len(hand)
        if n%groupSize!=0:
            return False
        if groupSize==1:
            return True
        hand.sort()
        queue=hand
        while queue:
            new=[]
            val=queue[0]
            size =1
            for i in range(1,len(queue)):
                if val+1==queue[i]:
                    val=queue[i]
                    size +=1
                    if size==groupSize:
                        break
                else:
                    new.append(queue[i])
            if size==groupSize:
                queue=new+queue[i+1:]
            else:
                print(queue)
                return False
        return True
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        handCounter = defaultdict(int)
        for val in hand:
            handCounter[val] += 1
            
        allKeys =  list(handCounter.keys())
        heapq.heapify(allKeys)
        
        while allKeys:
            cur=allKeys[0]
            
            for i in range(cur,cur+groupSize):
                if i not in handCounter:
                    return False
                handCounter[i]-=1
                if handCounter[i]==0:
                    if i != allKeys[0]:
                        return False
                    heapq.heappop(allKeys)
        return True
                    
                
        
        
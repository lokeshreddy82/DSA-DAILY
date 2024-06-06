class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res=[]
        for i in words[0]:
            flag=True
            for j in range(len(words)):
                if i in words[j]:
                    ind=words[j].index(i)
                    w=words[j]
                    if ind==0:
                        words[j]=w[1:]
                    else:
                        words[j]=w[0:ind]+w[ind+1:]
                else:
                    flag=False
            if flag:
                res.append(i)
        return res
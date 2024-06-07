class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        res=sentence.split(" ")
        print(res)
        hashing={}
        for i in dictionary:
            hashing[i]=1
        for ind,el in enumerate(res):
            replace=""
            for k in el:
                replace +=k
                if hashing.get(replace,0)!=0:
                    break
            res[ind]=replace
        return " ".join(res)

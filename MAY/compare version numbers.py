class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i=0
        j=0
        n1=len(version1)
        n2=len(version2)
        while i<n1 and j<n2:
            if version1[i]=="." and version2[j]==".":
                i +=1
                j +=1
                continue
            else:
                if version1[i]=="0":
                    for k in range(i+1,n1):
                        if version1[k]==".":
                            i=k-1
                            break
                        elif version1[k]!="0":
                            i=k
                            break
                if version2[j]=="0":
                    for m in range(j+1,n2):
                        if version2[m]==".":
                            j=m-1
                            break
                        elif version2[m]!="0":
                            j=m
                            break
                d1=n1
                for k in range(i+1,n1):
                    if version1[k]==".":
                        d1=k
                        break
                d2=n2
                for m in range(j+1,n2):
                    if version2[m]==".":
                        d2=m
                        break
                print(d1,d2)
                if int(version1[i:d1])>int(version2[j:d2]):
                    return 1
                if int(version1[i:d1])<int(version2[j:d2]):
                    return -1
                i =d1+1
                j=d2+1
        while i<n1:
            if version1[i]!='0' and version1[i]!='.':
                return 1
                print("end")
            i +=1
        while j<n2:
            if version2[j]!='0' and version2[j]!='.':
                return -1
                print("end")
            j +=1
        return 0
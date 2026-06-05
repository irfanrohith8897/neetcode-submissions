class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        string1={}
        string2={}
        if len(s1)>len(s2):
            return False

        for i in range(len(s1)):
            string1[s1[i]]=1+string1.get(s1[i],0)
            string2[s2[i]]=1+string2.get(s2[i],0)

        if string1==string2:
            return True

        l=0
        for r in range(len(s1),len(s2)):
            string2[s2[r]]=1+string2.get(s2[r],0)

            string2[s2[l]]-=1
            if string2[s2[l]]==0:
                del string2[s2[l]]
            l+=1

            if string1==string2:
                return True
        return string1==string2





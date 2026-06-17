class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        arr1=[0]*26
        arr2=[0]*26
        l=0
        r=len(s1)
        for i in range(len(s1)):
            arr1[ord(s1[i])%26]+=1
            arr2[ord(s2[i])%26]+=1
        
        while r<len(s2):
            if arr1==arr2:
                return True
            arr2[ord(s2[l])%26]-=1
            l+=1
            arr2[ord(s2[r])%26]+=1
            r+=1
        
        
        return arr1==arr2
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        arr=[0]*26
        for ch in s1:
            arr[ord(ch)%97]+=1
        l=0
        r=0
        word=[0]*26
        while r<len(s1):
            word[ord(s2[r])%97]+=1
            r+=1
        
        while r<len(s2):
            if arr==word:
                return True
            word[ord(s2[l])%97]-=1
            l+=1
            word[ord(s2[r])%97]+=1
            r+=1
        
        return arr==word
            
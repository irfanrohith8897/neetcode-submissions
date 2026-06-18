from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s:return ""

        dict1=Counter(t)
        need=len(dict1)

        dict2={}
        formed=0
        
        substr=(0,0)
        length=float('inf')
        l=0

        for r in range(len(s)):
                dict2[s[r]]=dict2.get(s[r],0)+1
                if s[r] in dict1 and  dict2[s[r]]==dict1[s[r]]:
                    formed+=1
                while l<=r and formed==need :
                    if r-l+1<length:
                        length=r-l+1
                        substr=(l,r)

                    dict2[s[l]]-=1
                    if s[l] in dict1 and dict2[s[l]]<dict1[s[l]]:
                        formed-=1
                    l+=1
        if length==float('inf'):
            return ""
        return s[substr[0]:substr[1]+1]
                
                

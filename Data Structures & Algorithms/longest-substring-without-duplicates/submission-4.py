class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        l=0
        r=1
        d={}
        d[s[l]]=1
        res=1
        while r<len(s):
            if s[r] not in d:
                d[s[r]]=1
            else:
                while s[l]!=s[r]:
                    d[s[l]]-=1
                    if d[s[l]]==0:
                        del d[s[l]]
                    l+=1
                l+=1
            res=max(res,r-l+1)
            r+=1
        return res




        
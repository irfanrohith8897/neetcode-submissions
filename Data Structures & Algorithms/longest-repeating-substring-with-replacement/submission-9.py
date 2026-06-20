class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        maxLen=0
        res=0
        d={}
        while l<=r and r<len(s):
            d[s[r]]=d.get(s[r],0)+1
            maxLen=max(maxLen,d[s[r]])

            while (r-l+1)-maxLen>k:
                d[s[l]]-=1
                l+=1
            res=max(r-l+1,res)
            r+=1
        return res
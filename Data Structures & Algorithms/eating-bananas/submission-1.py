import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res=0
        l=1
        r=max(piles)
        while l<=r:
            m=(l+r)//2
            t=0
            for pile in piles:
                t+=math.ceil(pile/m)
            if t<=h:
                res=m
                r=m-1
            else:
                l=m+1
        
        return res
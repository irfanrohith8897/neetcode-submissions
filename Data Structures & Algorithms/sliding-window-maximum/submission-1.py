import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        for i in range(k):
            heapq.heappush(res,(-nums[i],i))
        ans=[]
        l=0
        r=k-1
        while r<len(nums):
            while res[0][1]<l:
                heapq.heappop(res)
            ans.append(-res[0][0])
            l+=1
            r+=1
            if r<len(nums):
                heapq.heappush(res,(-nums[r],r))
        return ans

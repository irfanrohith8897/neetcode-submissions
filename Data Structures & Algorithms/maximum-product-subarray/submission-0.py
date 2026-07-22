class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev_maximum=nums[0]
        prev_minimum=nums[0]
        res=nums[0]
        for i in range(1,len(nums)):
            oldmax=prev_maximum
            oldmin=prev_minimum
            prev_maximum=max(nums[i],oldmax*nums[i],oldmin*nums[i])
            prev_minimum=min(nums[i],oldmax*nums[i],oldmin*nums[i])
            res=max(prev_maximum,res)
        return max(res,prev_maximum)
        
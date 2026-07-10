class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def solve(nums):
            prev2=0
            prev1=nums[0]
            for i in range(1,len(nums)):
                take=nums[i]+prev2
                nottake=prev1
                cur=max(take,nottake)
                prev2=prev1
                prev1=cur
            return prev1

        temp1=nums[1:]
        temp2=nums[0:len(nums)-1]
        return max(solve(temp1),solve(temp2))

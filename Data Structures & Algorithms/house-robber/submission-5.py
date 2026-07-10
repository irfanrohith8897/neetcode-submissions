class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        # dp=[None for _ in range(len(nums))]
        # def solve(idx):
        #     if idx>=len(nums):
        #         return 0
        #     if dp[idx] is not None:
        #         return dp[idx]

        #     left=solve(idx+1)
        #     right=nums[idx]+solve(idx+2)
        #     dp[idx]=max(left,right)
        #     return dp[idx]
        # return solve(0)

        # -------------2-----------
        # dp=[None for _ in range(len(nums))]
        # dp[0]=nums[0]
        # for i in range(1,len(nums)):
        #     left=dp[i-1]
        #     right=nums[i]
        #     if i>1:
        #         right+=dp[i-2]
        #     dp[i]=max(left,right)
        # return dp[-1]


        # -----------3--------------
        prev2=nums[0]
        prev1=max(nums[1],nums[0])
        for i in range(2,len(nums)):
            take=nums[i]+prev2
            nottake=prev1
            cur=max(take,nottake)
            prev2=prev1
            prev1=cur
        return prev1








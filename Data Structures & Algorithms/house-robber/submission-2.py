class Solution:
    def rob(self, nums: List[int]) -> int:
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
        dp=[None for _ in range(len(nums))]
        dp[0]=nums[0]
        for i in range(1,len(nums)):
            left=dp[i-1]
            right=nums[i]
            if i>1:
                right+=dp[i-2]
            dp[i]=max(left,right)
        return dp[-1]

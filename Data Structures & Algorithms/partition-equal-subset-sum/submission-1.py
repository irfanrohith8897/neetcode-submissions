class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        dp=[[None]*(total+1) for _ in range(len(nums))]
        def solve(i,cursum):
            if total-cursum==cursum:
                return True
            if i==len(nums):
                return False
            if dp[i][cursum] is not None:
                return dp[i][cursum]
            #take
            take=solve(i+1,cursum+nums[i])
            #nottake
            nottake=solve(i+1,cursum)

            dp[i][cursum]=take or nottake

            return take or nottake
        return solve(0,0)

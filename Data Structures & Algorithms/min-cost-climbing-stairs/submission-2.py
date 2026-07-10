class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[None for _ in range(len(cost))]
        def solve(idx):
            if idx>=len(cost):
                return 0
            if dp[idx] is not None:
                return dp[idx]

            left=solve(idx+1)
            right=solve(idx+2)

            dp[idx]=min(left,right)+cost[idx]
            return dp[idx]
            
        return min(solve(0),solve(1))
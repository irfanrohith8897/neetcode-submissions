class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[None for _ in range(len(cost))]

        def solve(idx):
            if idx==0:
                return cost[idx]
            if idx==1:
                return cost[idx]
            if dp[idx] is not None:
                return dp[idx]
                
            left=solve(idx-1)
            right=solve(idx-2)

            dp[idx]=min(left,right)+cost[idx]
            return dp[idx]

        return min(solve(len(cost)-1),solve(len(cost)-2))
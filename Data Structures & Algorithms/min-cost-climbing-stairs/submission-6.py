class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp=[None for _ in range(len(cost))]

        # def solve(idx):
        #     if idx==0:
        #         return cost[idx]
        #     if idx==1:
        #         return cost[idx]
        #     if dp[idx] is not None:
        #         return dp[idx]

        #     left=solve(idx-1)
        #     right=solve(idx-2)

        #     dp[idx]=min(left,right)+cost[idx]
        #     return dp[idx]

        # return min(solve(len(cost)-1),solve(len(cost)-2))

        # ---------2-----------
        # dp=[None for _ in range(len(cost))]
        # dp[0]=cost[0]
        # dp[1]=cost[1]
        prev1=cost[1]
        prev2=cost[0]
        for i in range(2,len(cost)):
            cur=min(prev1,prev2)+cost[i]
            prev2=prev1
            prev1=cur
        
        return min(prev1,prev2)
        







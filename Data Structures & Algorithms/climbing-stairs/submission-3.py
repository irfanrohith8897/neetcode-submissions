class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1)
        def memoization(n,dp):
            if n==0:
                return 1
            if dp[n]!=-1:
                return dp[n]
            l=memoization(n-1,dp)
            r=0
            if n>1:
                r=memoization(n-2,dp)
            
            dp[n]=l+r
            return l+r
        return memoization(n,dp)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[None for _ in range(n)] for _ in range(m)]
        def solve(i,j):
            if i==0 and j==0:
                return 1
            if dp[i][j] is not None:
                return dp[i][j]
            left=0
            if j>=1:
                left=solve(i,j-1)
            up=0
            if i>=1:
                up=solve(i-1,j)
            dp[i][j]=left+up
            return left+up
        return solve(m-1,n-1)
        
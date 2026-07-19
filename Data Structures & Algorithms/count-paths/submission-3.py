class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp=[[None for _ in range(n)] for _ in range(m)]
        # def solve(i,j):
        #     if i==0 and j==0:
        #         return 1
        #     if dp[i][j] is not None:
        #         return dp[i][j]
        #     left=0
        #     if j>=1:
        #         left=solve(i,j-1)
        #     up=0
        #     if i>=1:
        #         up=solve(i-1,j)
        #     dp[i][j]=left+up
        #     return left+up
        # return solve(m-1,n-1)


        # ---------2------Tabulation--------
        prev=[1 for _ in range(n)]
        # for i in range(n):
        #     dp[0][i]=1
        for i in range(1,m):
            cur=[0 for _ in range(n)]
            for j in range(n):
                up=prev[j]
                left=0
                if j>0:
                    left=cur[j-1]
                cur[j]=left+up
            prev=cur
        return prev[-1]

        
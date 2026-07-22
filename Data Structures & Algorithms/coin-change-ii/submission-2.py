class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        count=0
        n=len(coins)
        dp=[[None for _ in range(amount+1)] for _ in range(len(coins))]
        def solve(i,cursum):
            nonlocal n
            if cursum==amount:
                return 1
            if cursum>amount or i==n:
                return 0
            if dp[i][cursum]:
                return dp[i][cursum]

            add=solve(i,cursum+coins[i])

            skip=solve(i+1,cursum)
            dp[i][cursum]=add+skip

            return add+skip
        return solve(0,0)
        
         
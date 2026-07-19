class Solution:
    def numDecodings(self, s: str) -> int:
        dp=[None for _ in range(len(s))]
        def solve(idx):
            if idx>=len(s):
                return 1
            if s[idx] == "0":
                return 0
            if dp[idx] is not None:
                return dp[idx]

            double=0
            if idx<len(s)-1 and 1<=int(s[idx:idx+2])<=26:
                double=solve(idx+2)
            single=0
            if 1<=int(s[idx:idx+1])<=26:
                single=solve(idx+1)
            dp[idx]=single+double
            
            return single+double

        return solve(0)

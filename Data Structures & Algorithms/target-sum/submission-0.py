class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def solve(idx,cursum):
            if idx==len(nums):
                if cursum==target:
                    return 1
                return 0
            add=solve(idx+1,cursum+nums[idx])
            minus=solve(idx+1,cursum-nums[idx])

            return add+minus
        return solve(0,0)
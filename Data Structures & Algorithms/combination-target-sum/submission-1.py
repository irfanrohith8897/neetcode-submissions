class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def solve(idx,subset,target):
            if target==0:
                res.append(subset[:])
                return
            if target<0 or len(nums)==idx:
                return

            subset.append(nums[idx])
            solve(idx,subset,target-nums[idx])

            subset.pop()
            solve(idx+1,subset,target)
        
        solve(0,[],target)

        return res
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def solve(nums,idx,subset,target):
            if sum(subset)==target and idx<=len(nums):
                res.append(subset[:])
                return
            elif idx == len(nums) or sum(subset)>target:
                return
            subset.append(nums[idx])
            solve(nums,idx,subset,target)

            subset.pop()
            solve(nums,idx+1,subset,target)
        
        solve(nums,0,[],target)

        return res
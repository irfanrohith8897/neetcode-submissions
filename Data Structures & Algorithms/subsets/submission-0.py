class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def solve(i,nums,s):
            nonlocal res
            if i>=len(nums):
                res.append([i for i in s])
                return
            #not take
            solve(i+1,nums,s)

            #take
            s.append(nums[i])
            solve(i+1,nums,s)
            s.pop()
        solve(0,nums,[])

        return res
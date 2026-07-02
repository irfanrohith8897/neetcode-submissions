class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        isvisited=[False]*len(nums)
        def backtrack(subset):
            if len(subset)==len(nums):
                res.append(subset[:])
                return


            for i in range(0,len(nums)):
                if isvisited[i]==False:
                    isvisited[i]=True
                    subset.append(nums[i])
                    backtrack(subset)
                    subset.pop()
                    isvisited[i]=False
                # backtrack(idx+1,subset)
        backtrack([])
        return res
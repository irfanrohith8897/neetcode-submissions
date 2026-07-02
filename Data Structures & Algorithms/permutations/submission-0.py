class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        isvisited=[False]*len(nums)
        def backtrack(idx,subset):
            if len(subset)==len(nums):
                res.append(subset[:])
                return
            if idx==len(nums):
                return


            for i in range(0,len(nums)):
                if isvisited[i]==False:
                    isvisited[i]=True
                    subset.append(nums[i])
                    backtrack(i,subset)
                    subset.pop()
                    isvisited[i]=False
                # backtrack(idx+1,subset)
        backtrack(0,[])
        return res
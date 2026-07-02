class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def solve(idx,subset,target):
            if target==0:
                res.append(subset[:])
                return
            if target<0 or len(candidates)==idx:
                return

            #take
            subset.append(candidates[idx])
            solve(idx+1,subset,target-candidates[idx])
            subset.pop()

            #skipping dupplicates
            while idx+1<len(candidates) and candidates[idx]==candidates[idx+1]:
                idx+=1
            solve(idx+1,subset,target)
        
        solve(0,[],target)

        return res
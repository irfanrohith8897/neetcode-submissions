class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        res=[]
        d={2:"abc",3:"def",4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        def backtrack(idx,curStr):
            if len(curStr)==len(digits):
                res.append(curStr)
                return
            
            for ch in d[int(digits[idx])]:
                backtrack(idx+1,curStr+ch)
        
        backtrack(0,"")

        return res
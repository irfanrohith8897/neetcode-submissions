class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def backtrack(oc,cc,string):
            if len(string)==n*2:
                res.append(string)
                return
            if oc<n:
                backtrack(oc+1,cc,string+"(")
            if oc>cc:
                backtrack(oc,cc+1,string+")")
        backtrack(0,0,"")
        return res
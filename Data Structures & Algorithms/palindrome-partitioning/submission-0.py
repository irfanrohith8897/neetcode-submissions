class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(string):
            return string==string[::-1]
        res=[]
        def backtrack(i,curlist):
            if i==len(s):
                res.append(curlist[:])
                return


            for j in range(i,len(s)):
                substring=s[i:j+1]
                if isPalindrome(substring):
                    curlist.append(substring)
                    backtrack(j+1,curlist)
                    curlist.pop()
        backtrack(0,[])
        return res
                
            
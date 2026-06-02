class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls=''
        rs=''
        for ch in s:
            if ch.isalnum():
                ls+=ch
                rs=ch+rs
        return ls.lower()==rs.lower()
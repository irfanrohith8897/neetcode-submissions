class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=0
        substr=''
        for i in range(len(s)):
            if s[i] in substr:
                while s[i] in substr:
                    substr=substr[1:]

            substr+=s[i]

            length=max(length,len(substr))
        return length
        


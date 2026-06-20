class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for char in s:
            if char in ['[','(','{']:
                stack.append(char)
            else:
                if len(stack)==0:
                    return False
                else:
                    if (char==']' and stack[-1]=='[') or (char==')' and stack[-1]=='(') or (char=='}' and stack[-1]=='{'):
                        stack.pop()
                    else:
                        stack.append(char)
                        
        return len(stack)==0

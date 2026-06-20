class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]

        for i in range(len(temperatures)-1,-1,-1):

            while stack and temperatures[stack[-1]]<=temperatures[i]:
                stack.pop()

            if not stack:
                res[i]=0
            else:
                res[i]=stack[-1]-i

            if not stack or temperatures[i]< temperatures[stack[-1]]:
                stack.append(i)
            
            
        print(stack)
        return res

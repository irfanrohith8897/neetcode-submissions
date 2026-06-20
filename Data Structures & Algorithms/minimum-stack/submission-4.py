class MinStack:

    def __init__(self):
        self.stack=[]
        self.mini=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mini)==0 or val<=self.mini[-1]:
            self.mini.append(val)

    def pop(self) -> None:
        if self.stack[-1]==self.mini[-1]:
            self.mini.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini[-1]

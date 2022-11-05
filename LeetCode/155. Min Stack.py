class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = [] 

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0 or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        if len(self.stack) !=0:
            pop = self.stack.pop()
            if pop in self.minStack and pop == self.minStack[-1]:
                self.minStack.remove(pop)

    def top(self) -> int:
        if len(self.stack) >=1:
            top = self.stack[-1]
            return top

    def getMin(self) -> int:
        if len(self.minStack) >=1:
            return self.minStack[-1]
        else:
            return "null"
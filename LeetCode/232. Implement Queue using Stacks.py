class MyQueue:

    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(x)
            return
        
        while self.stack:
            temp = self.stack.pop(-1)
            self.stack2.append(temp)
            
        self.stack.append(x)
        
        while self.stack2:
            self.stack.append(self.stack2.pop(-1))

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop(-1)

    def peek(self) -> int:
        if self.stack:
            return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0
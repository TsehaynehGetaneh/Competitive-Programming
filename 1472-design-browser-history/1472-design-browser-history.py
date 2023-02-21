class Node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = Node(homepage)
        self.curr = self.homepage
        self.length = 1
    def visit(self, url: str) -> None:
        self.curr.next = Node(url)
        self.curr = self.curr.next
        self.length += 1

    def back(self, steps: int) -> str:
        start_idx = 1
        newSteps = self.length - steps
        self.curr = self.homepage
        
        while start_idx < newSteps:
            self.curr = self.curr.next
            start_idx += 1
        
        self.length =  start_idx
        
        return self.curr.val

    def forward(self, steps: int) -> str:
        i = 0
        newLength = 0
        while self.curr and self.curr.next and i < steps:
            self.curr = self.curr.next
            i += 1
            newLength += 1
        
        self.length += newLength
        
        return self.curr.val    


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
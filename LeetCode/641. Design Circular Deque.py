class MyCircularDeque:

    def __init__(self, k: int):
        self.front = -1
        self.rear = 0
        self.size = k
        self.deque = [None] *k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            if self.front == -1:
                self.front = 0
                self.rear = 0
            elif self.front == 0:
                self.front = self.size -1
            else:
                self.front -=1
            self.deque[self.front] = value
            return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            if self.front == -1:
                self.front = 0
                self.rear = 0
            elif self.rear == self.size -1:
                self.rear = 0
            else:
                self.rear = self.rear +1
            self.deque[self.rear] = value
            return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                if self.front == self.size -1:
                    self.front = 0
                else:
                    self.front = self.front +1
            self.deque[self.front]
            return True

    def deleteLast(self) -> bool:
        if (self.isEmpty()):
            return False
        if (self.front == self.rear):
            self.front = -1
            self.rear = -1
        elif (self.rear == 0):
            self.rear = self.size-1
        else:
            self.rear = self.rear-1
        self.deque[self.rear]
        return True

    def getFront(self) -> int:
        if (self.isEmpty()):
            return -1
 
        return self.deque[self.front]

    def getRear(self) -> int:
        if(self.isEmpty() or self.rear < 0):
            return -1
 
        return self.deque[self.rear]

    def isEmpty(self) -> bool:
        if self.front == -1:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if (self.front == 0 and self.rear == self.size -1) or (self.front == self.rear +1):
            return True
        else:
            return False
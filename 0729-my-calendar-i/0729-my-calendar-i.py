class MyCalendar:

    def __init__(self):
        self.books = []
        

    def book(self, start: int, end: int) -> bool:
        if not self.books:
            self.books.append((start,end))
            
            return True
        # sort
        # self.books.sort()

        for s, e in self.books:
            if not (end <= s or start >= e):
                return False

        else:
            self.books.append((start, end))

        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
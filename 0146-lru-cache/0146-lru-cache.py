class LRUCache:

    def __init__(self, capacity: int):
        self.capcaity = capacity 
        self.cache = deque()
        self.dic = {}
        

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        self.cache.remove(key)
        self.cache.appendleft(key)
        value = self.dic[key]
        return value
        

    def put(self, key: int, value: int) -> None:
        if key not in self.dic:
            if len(self.cache ) == self.capcaity:
                oldest = self.cache.pop()
                del self.dic[oldest]

                self.dic[key] = value
                self.cache.appendleft(key)
            else:
                

                self.dic[key] = value
                self.cache.appendleft(key)

        else: 
            self.cache.remove(key)   

            self.dic[key] = value
            self.cache.appendleft(key)

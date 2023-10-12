class MyHashMap:

    def __init__(self):
        self.hashMap = []

    def put(self, key: int, value: int) -> None:
        is_key_found = False
        for i in range(len(self.hashMap)):
            k,v = self.hashMap[i]
            if key == k:
                is_key_found = True
                self.hashMap[i] = (key,value)
                break
                
        if not is_key_found:
            self.hashMap.append((key,value))

    def get(self, key: int) -> int:
        for i in range(len(self.hashMap)):
            k,v = self.hashMap[i]
            if k == key:
                return v
            
        return -1

    def remove(self, key: int) -> None:
         for i in range(len(self.hashMap)):
            k,v = self.hashMap[i]
            if k == key:
                self.hashMap.remove(self.hashMap[i])
                return 


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
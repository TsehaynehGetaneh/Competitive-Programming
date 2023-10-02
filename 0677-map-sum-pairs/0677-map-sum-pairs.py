class TrieNode:
    def __init__(self):
        self.children = [0] * 26
        self.visit_count = 0
        self.is_end = False

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.hashmap = {}

    def insert(self, key: str, val: int) -> None:
        if key in self.hashmap:
            ptr = self.root
            for char in key:
                idx = ord(char) - ord("a")
                ptr = ptr.children[idx]
                ptr.visit_count += (val - self.hashmap[key])
        else:
            current = self.root
            i = 0
            for char in key:
                idx = ord(char) - ord("a")

                if not current.children[idx]:
                    current.children[idx] = TrieNode()

                current = current.children[idx]
                current.visit_count += val


            current.is_end = True
        
        self.hashmap[key] = val

    def sum(self, prefix: str) -> int:
        current = self.root
        
        for pre in prefix:
            idx = ord(pre) - ord("a")
            if current.children[idx]:
                current = current.children[idx]
            else:
                return 0
            
        return current.visit_count
        

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
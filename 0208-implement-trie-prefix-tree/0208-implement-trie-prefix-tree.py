class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]
      

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root

        for char in word:
            idx = ord(char) - ord("a")
            if not current.children[idx]:
                current.children[idx] = TrieNode()

            current = current.children[idx]

        current.is_end = True
        
    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for pre in prefix:
            idx = ord(pre) - ord("a")

            if not current.children[idx]:
                return False
            
            current = current.children[idx]

        return True


    def search(self, word: str) -> bool:
        current = self.root

        for char in word:
            idx = ord(char) - ord("a")

            if not current.children[idx]:
                return False
            
            current = current.children[idx]
            
        return current.is_end
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
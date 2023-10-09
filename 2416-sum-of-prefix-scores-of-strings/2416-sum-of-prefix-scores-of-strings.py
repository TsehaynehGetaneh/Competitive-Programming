class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.count = 0
        
class Solution:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        current = self.root
        for char in word:
            idx = ord(char) - ord("a")
            
            if not current.children[idx]:
                current.children[idx] = TrieNode()
                
            current = current.children[idx]
            current.count += 1
        
    def score(self,word):
        total_count = 0
        
        current = self.root
        for char in word:
            idx = ord(char) - ord("a")
            
            current = current.children[idx]
            total_count += current.count
            
        return total_count
        
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # insert words
        for word in words:
            self.insert(word)
            
        ans = []
        # count score
        for word in words:
            count = self.score(word)
            ans.append(count)
            
        return ans
        
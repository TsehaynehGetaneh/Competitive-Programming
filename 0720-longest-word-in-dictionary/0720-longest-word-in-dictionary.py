class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self,word):
        current = self.root
        
        for char in word:
            idx = ord(char) - ord("a")
            
            if not current.children[idx]:
                current.children[idx] = TrieNode()
                
            current = current.children[idx]
      
        current.is_end = True


class Solution:
    def longestWord(self, words: List[str]) -> str:
        obj = Trie()
        for word in words:
            obj.insert(word)
        
        root = obj.root
        longest_word = ""
            
        def dfs(ptr,word):
            nonlocal longest_word
            # base cases
            if not ptr.children or (ptr != root and not ptr.is_end):
                return 
            
            
            for i in range(26):
                if ptr.children[i] and ptr.children[i].is_end:
                    ch = chr(ord("a") + i)
                    if len(word+ch) > len(longest_word):
                        longest_word = word + ch
                    
                    dfs(ptr.children[i],word+ch)
                    
        dfs(obj.root,"")
        
        return longest_word
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
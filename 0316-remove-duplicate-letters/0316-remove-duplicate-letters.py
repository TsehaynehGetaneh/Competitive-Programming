class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = Counter(s)
        stack = []
        set_ = set()
        
        for char in s:
            if char in set_:
                freq[char] -= 1
                continue
            
            while stack and char < stack[-1] and freq[stack[-1]] > 1:
                popped = stack.pop()
                set_.remove(popped)
                freq[popped] -= 1
            
            stack.append(char)
            set_.add(char)
            
        return "".join(stack)
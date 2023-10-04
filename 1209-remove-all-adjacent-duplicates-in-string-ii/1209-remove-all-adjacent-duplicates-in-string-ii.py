class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        hmap = defaultdict(int)
        
        for char in s:
            stack.append(char)
            hmap[char] += 1
            current_char = char
            
            while hmap[current_char] >= k and stack[len(stack)-k:].count(current_char)==k:
                j = 0
                while j < k:
                    hmap[current_char] -= 1
                    stack.pop()
                    j += 1
                    
                if len(stack)>=k:   
                    current_char = stack[-1]
                else:
                    break
                
        return "".join(stack)
                
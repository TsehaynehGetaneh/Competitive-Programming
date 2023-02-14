class Solution:
    def makeGood(self, s: str) -> str:
        chars = []
        
        for i in range(len(s)):
            char = s[i]
            small = char.lower()
            cap = char.upper()
            
            if not chars:
                chars.append(char)
            elif char == small:
                if chars[-1] == cap:
                    chars.pop()
                else:
                    chars.append(char)
            elif char == cap:
                if chars[-1] == small:
                    chars.pop()
                else:
                    chars.append(char)
            else:
                chars.append(char)
                
                    
        return "".join(chars)
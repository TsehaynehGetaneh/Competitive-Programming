class Solution:
    def removeStars(self, s: str) -> str:
        new_s = []
        
        for i in range(len(s)):
            if not new_s:
                new_s.append(s[i])
            else:
                if s[i] == "*":
                    if new_s:
                        new_s.pop()
                else:
                    new_s.append(s[i])
                    
        return ''.join(new_s)
        
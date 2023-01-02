class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        output = ''
        idx = 0
        for i in range(len(spaces)):
            output += s[idx:spaces[i]]
            output += " "
            idx = spaces[i]
            
        if idx < len(s):
            output += s[idx:]
            
        return output
            
        
        
        
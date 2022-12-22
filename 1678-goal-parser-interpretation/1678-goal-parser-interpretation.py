class Solution:
    def interpret(self, command: str) -> str:
        res = ''
        
        i = 0
        while i < len(command):
            if command[i] == "G":
                res += "G"
                i += 1
            elif (i+1) < len(command) and command[i] == "(" and command[i+1] == ")":
                res += "o"
                i += 2
            else:
                res += "al"
                i += 4
        return res
                
            
        
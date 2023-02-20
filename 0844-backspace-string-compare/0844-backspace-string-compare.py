class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        str1 = []
        str2 = []
        
        i = 0
        while i < len(s):
            if str1 and s[i] == "#":
                str1.pop()
            elif not str1 and s[i] == "#":
                pass
            else:
                str1.append(s[i])
                
            i += 1
        
        j = 0
        while j < len(t):
            if str2 and t[j] == "#":
                str2.pop()
            elif not str2 and t[j] == "#":
                pass
            else:
                str2.append(t[j])
                
            j += 1
        print(str1,str2)    
        if "".join(str1) == "".join(str2):
            return True
        else:
            return False
class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        print(s)
        output = []
        
        maxWord = float("-inf")
        for word in s:
            if len(word) > maxWord:
                maxWord = len(word)
                
        for i in range(maxWord):
            word = ''
            for j in range(len(s)):
                if i < len(s[j]):
                    word += s[j][i]
                else:
                    word += " "
            
            output.append(word)
        
        ans = []
        for word in output:
            ans.append(word.rstrip())
            
        return ans
            
        
class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = 'aeiou'
        count = 0
        
        def backtrack(idx,string):
            nonlocal count
            if idx > 5:
                return
            
            if len(string) == n:
                count += 1
                return 
            
            
            for i in range(idx,5):
                backtrack(i,string+vowels[i])
                
        backtrack(0,"")
        
        return count
            
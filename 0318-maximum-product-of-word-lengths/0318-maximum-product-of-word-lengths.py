class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        max_len = 0
        arr = []
        for i in range(len(words)):
            num = 0
            for char in words[i]:
                num|= 1<< (ord(char) - ord('a'))
            
            arr.append(num)
            
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if not (arr[i] & arr[j]):
                    max_len = max(max_len, len(words[i]) * len(words[j]))
        return max_len
                
                    
                
        
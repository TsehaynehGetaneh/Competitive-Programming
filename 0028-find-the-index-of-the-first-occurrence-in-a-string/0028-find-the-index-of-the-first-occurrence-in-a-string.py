class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            j = 0
            k = i
            while j < len(needle) and k < len(haystack):
                if haystack[k] != needle[j]:
                    break
                    
                else:
                    j += 1
                    k += 1
                    
            if j == len(needle):
                return i
            
        return - 1
        
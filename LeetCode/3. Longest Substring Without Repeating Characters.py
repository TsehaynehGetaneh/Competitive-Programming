class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windowString = set()
        right =0
        left =0
        longest = 1
        
        if len(s) == 0:
            return 0
        
        while left < len(s) and right< len(s):
            if s[right] not in windowString:
                windowString.add(s[right])
                right +=1
                longest = max(longest, right - left)
            else:
                windowString.remove(s[left])
                left +=1
                
        return longest
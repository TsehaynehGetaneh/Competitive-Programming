class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = "aeiou"
        count = 0
        for char in range(k):
            if s[char] in vowels:
                count +=1
        maxCount = count

        
        i = 1
        j = i + k-1
        while (j-i) +1 == k and j<len(s):
            if s[i-1] in vowels:
                count -=1
            if s[j] in vowels:
                count +=1
            maxCount = max(count, maxCount)
            i +=1
            j +=1
        return maxCount
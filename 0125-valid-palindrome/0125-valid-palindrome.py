class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaNum = ''.join(ch for ch in s if ch.isalnum()).lower()
        n = len(alphaNum)
        str1 = alphaNum[:n//2]
        str2 = ''
        if n%2 !=0:
            str2 = alphaNum[n-1: n//2:-1]
        else:
            str2 = alphaNum[n-1:n//2 -1: -1]
        return str1 == str2
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if len(word)%2 == 0:
                first_part = word[:len(word)//2]
                second_part = word[len(word)//2:]
                if first_part == second_part[::-1]:
                    return word
                
            else:
                first_part = word[:len(word)//2]
                second_part = word[len(word)//2+1:]
                if first_part == second_part[::-1]:
                    return word
                
        return ""
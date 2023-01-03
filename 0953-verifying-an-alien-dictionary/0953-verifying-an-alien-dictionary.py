class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}
        val = 1
        for char in order:
            dic[char] = val
            val += 1
        if len(words) == 1:
            return True
        
        left = 0
        right = 1
        while left < right and right < len(words):
            l_word = list(words[left])
            r_word = list(words[right])
            length = min(len(l_word), len(r_word))
            for i in range(length):
                if i == length-1 and dic[l_word[i]] == dic[r_word[i]] and len(r_word) == length and len(l_word) != length:
                    return False
                elif dic[l_word[i]] < dic[r_word[i]]:
                    break
                elif dic[l_word[i]] > dic[r_word[i]]:
                    return False
            left += 1
            right += 1
            
        return True
        
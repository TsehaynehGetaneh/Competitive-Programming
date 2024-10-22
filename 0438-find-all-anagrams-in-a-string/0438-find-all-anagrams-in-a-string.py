class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        counter_p = Counter(p)
        counter_s = Counter(s[:len(p)])
        j = 0

        res = []
        if counter_p == counter_s:
            res.append(j)
        
        for i in range(len(p), len(s)):
            counter_s[s[j]] -= 1
            counter_s[s[i]] += 1

            j += 1
            if counter_s == counter_p:
                res.append(j)

        return res



        
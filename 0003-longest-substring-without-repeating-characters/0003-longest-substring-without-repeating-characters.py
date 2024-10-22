class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict

        d = defaultdict(int)
        j = 0
        res = 0
        for i in range(len(s)):
            d[s[i]] += 1
            while j<=i and d[s[i]] > 1:
                d[s[j]] -= 1
                j += 1

            res = max(res, i-j+1)

        return res
        
class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        indices = []
        total = 0

        for i in range(len(s)):
            if s[i] == c:
                indices.append(i)

        for i in range(len(indices)):
            total += (i+1)

        return total


        
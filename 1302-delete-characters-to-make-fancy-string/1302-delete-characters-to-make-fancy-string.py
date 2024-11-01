class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s

        arr = [s[0], s[1]]
        for i in range(2, len(s)):
            if not (s[i] == s[i-1] == s[i-2]):
                arr.append(s[i])

        return "".join(arr)
        
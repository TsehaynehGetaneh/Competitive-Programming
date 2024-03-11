class Solution:
    def customSortString(self, order: str, s: str) -> str:
        data = {}

        for i in range(len(order)):
            data[order[i]] = i

        arr = []

        for i in range(len(s)):
            if s[i] in data:
                arr.append([data[s[i]], s[i]])
            else:
                arr.append([len(order), s[i]])

        arr.sort()

        res = []
        for i in range(len(arr)):
            res.append(arr[i][1])

        return "".join(res)
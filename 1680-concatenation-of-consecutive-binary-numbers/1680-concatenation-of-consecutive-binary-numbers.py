class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = []

        for i in range(1, n+1):
            res.append(bin(i)[2:])

        res = "0b" + "".join(res)
        
        return int(res,2)% (10**9 + 7)
        
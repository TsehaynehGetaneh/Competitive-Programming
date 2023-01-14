class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)[::-1]
        if x[-1] == "-":
            x = int(x[:-1]) * -1
            if x < -2**31 or x >= 2**31 -1:
                return 0
            else:
                return x
        else:
            if int(x) < -2**31 or int(x) >= 2**31 -1:
                return 0
            else:
                return int(x)
        
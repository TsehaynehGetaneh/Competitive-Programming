class Solution:
    def addDigits(self, num: int) -> int:
        num_str = str(num)

        while len(num_str) > 1:
            res = 0
            for digit in num_str:
                res += int(digit)

            num_str = str(res)

        return int(num_str)

        
class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        total = 0

        for num in nums:
            l = len(str(num))
            num = max(list(str(num))) * l

            total += int(num)

        return total
        
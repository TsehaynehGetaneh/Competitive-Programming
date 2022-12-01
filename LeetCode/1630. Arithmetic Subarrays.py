class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i in range(len(l)):
            temp = nums[l[i]:r[i] + 1]
            temp.sort()
            dif = temp[1] - temp[0]
            isArithmetic = True
            j = 1
            while j < len(temp):
                if temp[j] -temp[j-1] != dif:
                    isArithmetic = False
                    break
                j += 1

            res.append(isArithmetic)
        return res

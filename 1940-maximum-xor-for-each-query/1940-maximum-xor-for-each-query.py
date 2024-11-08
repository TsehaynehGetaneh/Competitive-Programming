class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        if len(nums) == 1:
            return [2**maximumBit - 1]
        res = []
        max_num = 2**maximumBit - 1
        sub_xor = 0

        for num in nums:
            sub_xor = (sub_xor ^ num)
            res.append(sub_xor ^ max_num)
       
        return res[::-1]

        
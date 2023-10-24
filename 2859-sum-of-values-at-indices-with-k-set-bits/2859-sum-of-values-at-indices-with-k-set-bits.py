class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        total = 0
        for i,num in enumerate(nums):
            if i.bit_count() == k:
                total += num
                
        return total
        
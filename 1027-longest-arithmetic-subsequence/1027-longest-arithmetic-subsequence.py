class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        cache = {} 

        for right in range(len(nums)):
            for left in range(0, right):
                diff = nums[right] - nums[left]
                
                if (left, diff) in cache:
                    cache[(right, diff)] = cache[(left, diff)] + 1
                else:
                    cache[(right, diff)] = 2 
        return max(cache.values())
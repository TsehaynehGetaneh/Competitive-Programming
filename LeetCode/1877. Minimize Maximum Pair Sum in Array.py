class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        start = 0
        end = len(nums) -1 
        res = nums[start] + nums[end]
        while start < end:
            if nums[start] + nums[end] > res:
                res = nums[start] + nums[end]
            start += 1
            end -= 1
        return res

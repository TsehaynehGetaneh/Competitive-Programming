class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        start = 0
        end = 0
        sub_sum = 0
        while start < len(nums):
            while end < len(nums) and sub_sum < target:
                sub_sum += nums[end]
                end += 1
            if sub_sum >= target:
                if res == 0:
                    res = end - start
                else:
                    res = min(res, end-start)
            sub_sum -= nums[start]
            start += 1
        return res

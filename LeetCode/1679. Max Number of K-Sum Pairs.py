class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        num_op = 0
        while left < right:
            pair_sum = nums[left] + nums[right]
            if pair_sum < k:
                left += 1
            if pair_sum > k:
                right -= 1
            if pair_sum == k:
                num_op += 1
                left += 1
                right -= 1
        return num_op

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {}

        def dp_helper(sub_sum):
            if sub_sum in dp:
                return dp[sub_sum]

            if sub_sum > target:
                return 0

            if sub_sum == target:
                return 1

            count = 0
            for i in range(len(nums)):
                count += dp_helper(sub_sum + nums[i])

            dp[sub_sum] = count
            return count

        return dp_helper(0)

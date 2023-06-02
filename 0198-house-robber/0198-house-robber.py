class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        
        dp = [nums[i] for i in range(len(nums))]
        
        for i in range(1,len(nums)):
            if i == 1:
                dp[i] = max(dp[i-1],dp[i])
            else:
                dp[i] = max(nums[i]+ dp[i-2],dp[i-1])
         
        return max(dp[-1],dp[-2])
        
        
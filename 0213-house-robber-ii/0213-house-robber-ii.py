class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        
        dp1 = [nums[i] for i in range(len(nums))]
        dp2 = [nums[i] for i in range(len(nums))]
        dp2[0] = 0
        
        for i in range(1,len(nums)):
            if i < len(nums) - 1:
                if i == 1:
                    dp1[i] = max(dp1[i-1],dp1[i])
                else:
                    dp1[i] = max(dp1[i-1], nums[i] + dp1[i-2])
                
            if i < len(nums):
                if i == 1:
                    dp2[i] = max(dp2[i-1],dp2[i])
                else:
                    dp2[i] = max(dp2[i-1], nums[i] + dp2[i-2])
                
        max1 = max(dp1[-1],dp1[-2])
        max2 = max(dp2[-1],dp2[-2])
        
        return max(max1,max2)
        
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        cache = {}
        
        def dp(idx,summ):
            if (idx,summ) in cache:
                return cache[(idx,summ)]
            
            if idx == n:
                return int(summ == target)
            
            cache[(idx,summ)] = dp(idx+1,summ+nums[idx]) + dp(idx+1,summ-nums[idx])
            
            return cache[(idx,summ)]
        
        return dp(0,0)
        
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0,1]
        if n == 0:
            return 0
        
        if n <= 1:
            return 1
        
        i = 1
        while i <= n//2:
            idx1 = 2*i
            idx2 = 2*i + 1
            
            val_idx1 = nums[i]
            nums.append(val_idx1)
            
            if len(nums) == n+1:
                return max(nums)
            
            val_idx2 = nums[i] + nums[i+1]
            nums.append(val_idx2)
            
            if len(nums) == n+1:
                return max(nums)
            
            i += 1
            
        
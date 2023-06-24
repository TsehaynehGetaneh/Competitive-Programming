class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        max_num = max(nums)
        min_num = min(nums)
        
        for num in nums:
            if num != min_num and num != max_num:
                return num
            
            
        return -1
        
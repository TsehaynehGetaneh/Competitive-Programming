class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = nums[0]
        summ = nums[0]
        
        for i in range(1,len(nums)):
            summ += nums[i]
            ans = max(ans,ceil(summ/(i+1)))
            
        return ans
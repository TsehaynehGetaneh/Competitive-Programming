class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = [0] * len(nums)
        right_sum = [0] * len(nums)
        ans = []
        
        for i in range(1,len(nums)):
            left_sum[i] = left_sum[i-1] + nums[i-1]
        
        for i in range(len(nums)-2,-1,-1):
            right_sum[i] = right_sum[i+1] + nums[i+1]
            
        for i in range(len(nums)):
            ans.append(abs((left_sum[i] - right_sum[i])))
            
        return ans
            
        
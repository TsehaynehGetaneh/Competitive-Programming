class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        maxSum = 0
        nums.sort()
        
        for i in range(len(nums)-2):
            subSum = 0
            
            if nums[i] + nums[i+1] > nums[i+2] and nums[i] + nums[i+2] > nums[i+1] and nums[i+2] + nums[i+1] > nums[i]:
                subSum = sum(nums[i:i+3])
                
            if subSum > maxSum:
                maxSum = subSum

        
        
        
        
        
        
        
        return maxSum
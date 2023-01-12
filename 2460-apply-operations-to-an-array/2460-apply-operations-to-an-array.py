class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                nums[i-1], nums[i] = nums[i-1]*2,0
                
        left = 0
        right = 1
        
        while right < len(nums):
            if nums[left] != 0:
                left += 1
                right += 1
            elif nums[right] == 0:
                right += 1
            else:
                nums[left],nums[right] = nums[right],nums[left]
                
        return nums
        
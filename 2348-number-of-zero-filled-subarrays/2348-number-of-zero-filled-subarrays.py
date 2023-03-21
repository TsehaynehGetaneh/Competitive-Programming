class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        left,right = 0,0
        count = 0
        
        while right < len(nums):
            if nums[right] == 0:
                left = right
                
                while right < len(nums) and nums[right] == 0:
                    count += (right-left+1)
                    right += 1
                
                left = right
            
            else:
                left += 1
                right += 1
                
              
        return count
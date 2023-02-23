class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = [nums[0]]
        
        for i in range(1,len(nums)):
            val = running_sum[-1] + nums[i]
            running_sum.append(val)
            
        return running_sum
            
            
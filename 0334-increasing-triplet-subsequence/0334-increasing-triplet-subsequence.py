class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        prev_min = [nums[0]] * len(nums)
        next_max = [nums[len(nums)-1]]*len(nums)
        
        for i in range(1,len(nums)):
            prev_min[i] = min(nums[i],prev_min[i-1])
            
            
        for i in range(len(nums)-2,-1,-1):
            next_max[i] = max(nums[i],next_max[i+1])
            
        for i in range(len(nums)):
            if prev_min[i] < nums[i] < next_max[i]:
                return True
            
        return False
        
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        output = []
        
        for i in range(len(nums)):
            idx = index[i]
            num = nums[i]
            
            output.insert(idx,num)
        
        return output
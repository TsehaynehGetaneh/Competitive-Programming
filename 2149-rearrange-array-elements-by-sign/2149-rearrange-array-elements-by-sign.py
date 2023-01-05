class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posetives = []
        negatives = []
        
        for i in range(len(nums)):
            if nums[i] > 0:
                posetives.append(nums[i])
            else:
                negatives.append(nums[i])
        print(posetives)
        print(negatives)
        idx = 0
        i = 0
        while i < len(nums)-1:
            nums[i] = posetives[idx]
            nums[i+1] = negatives[idx]
                
            i += 2
            idx += 1
            
        return nums
        
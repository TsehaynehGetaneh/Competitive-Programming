class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtrack(idx,arr):
            if idx > len(nums):
                return 
            
            ans.append(arr)
            
            for i in range(idx,len(nums)):
                backtrack(i+1,arr + [nums[i]])
                
                
        backtrack(0,[])
        
        return ans
            
            
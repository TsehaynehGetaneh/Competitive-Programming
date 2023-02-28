class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        table = [0 for _ in range(len(nums))]
        
        min_far = float('inf')
        for i, num in enumerate(nums):
            table[i] = min_far
            min_far = min(min_far, num)
        
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            while stack and stack[-1] < nums[i]:
                curr = stack.pop()
                
                if curr > table[i]:
                    return True
            stack.append(nums[i])
                    
        return False
                
        
        
         
        
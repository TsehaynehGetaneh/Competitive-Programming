class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_val = 0
        left = 0
        
        for right in range(1,len(values)):
            max_val = max(max_val,values[left]+values[right]+left-right)
            
            if (values[left]+left) < (values[right]+right):
                left = right
                
                
        return max_val
        
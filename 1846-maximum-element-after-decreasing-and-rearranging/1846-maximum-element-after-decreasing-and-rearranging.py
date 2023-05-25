class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr = sorted(arr)
        
        for i in range(len(arr)):
            if i == 0:
                arr[i] = 1
                
            else:
                if abs(arr[i]-arr[i-1]) > 1:
                    arr[i] = arr[i-1] + 1
        # print(arr)           
        return max(arr)
                    
                
            
        
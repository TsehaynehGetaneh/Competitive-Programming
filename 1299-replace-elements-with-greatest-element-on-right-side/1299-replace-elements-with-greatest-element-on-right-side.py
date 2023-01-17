class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = max(arr)
        idx = arr.index(max_val)
        
        for i in range(len(arr)):
            print(idx)
            if i == len(arr) -1:
                arr[i] = -1
            else:
                if idx > i:
                    arr[i] = max_val
                else:
                    max_val = max(arr[i+1:])
                    idx = arr.index(max_val)
                    
                    arr[i] = max_val
            
        return arr
        
        
            
        
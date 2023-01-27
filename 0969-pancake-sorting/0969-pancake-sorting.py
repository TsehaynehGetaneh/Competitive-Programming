class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
         # flip the array
        def flip_array(arr,idx):
            start = 0
            while start < idx:
                arr[start],arr[idx] = arr[idx],arr[start]

                start += 1
                idx -= 1

        # find max_value heper func
        def find_max(arr,n):
            idx = 0
            for i in range(n):
                if arr[idx] < arr[i]:
                    idx = i
            return idx
        
        
        output = []
        curr_length = len(arr)
        while curr_length > 1:
            max_idx = find_max(arr,curr_length)
            
            if max_idx != curr_length -1:
                flip_array(arr,max_idx)
                
                output.append(max_idx+1)
                
                flip_array(arr,curr_length-1)
             
                output.append(curr_length)
            curr_length -= 1
            
            
        return output
        
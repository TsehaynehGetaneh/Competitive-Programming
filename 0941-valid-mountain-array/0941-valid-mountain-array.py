class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        inc_arr = []
        dec_arr = []
        
        for i in range(1,len(arr)):
            if i == 1 and arr[i] <= arr[i-1]:
                dec_arr = arr
                return False
            if arr[i] <= arr[i-1]:
                inc_arr.extend(arr[:i])
                dec_arr.extend(arr[i:])
                break
            
        print(inc_arr,dec_arr)
        for i in range(1,len(dec_arr)):
            if dec_arr[i] >= dec_arr[i-1]:
                return False
        
        if len(inc_arr) == 0 or len(dec_arr) == 0 or len(arr) <2:
            return False
        
        if len(dec_arr) == 1:
            if dec_arr[0] == inc_arr[-1]:
                return False
        
        
        return True
                    
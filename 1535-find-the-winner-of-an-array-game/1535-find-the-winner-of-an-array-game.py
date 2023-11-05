class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k > len(arr):
            return max(arr)
        d = {}
        for num in arr:
            d[num] = 0
            
        i,j = 0,1
        while len(arr) > 1:
            val1 = arr[i]
            val2 = arr[j]
            
            if val1 > val2:
                arr.append(val2)
                j += 1
                
                d[val1] += 1
                
                if d[val1] == k:
                    return val1
                
            else:
                arr.append(val1)
                i = j
                j += 1
                
                d[val2] += 1
                
                if d[val2] == k:
                    return val2
        
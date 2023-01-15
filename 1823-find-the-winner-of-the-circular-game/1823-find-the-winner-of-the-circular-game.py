class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1,n+1)]
        
        while len(arr) > 1:
            i = (k-1)%len(arr)
            
            arr.pop(i)
            arr = arr[i:] + arr[:i]
                
        return arr[0]
            
        
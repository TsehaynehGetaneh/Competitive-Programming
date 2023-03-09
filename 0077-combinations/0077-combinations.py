class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(idx,arr):
            if len(arr) == k:
                res.append(arr)
                return
                
            for i in range(idx,n+1):
                backtrack(i+1,arr + [i])
                
        backtrack(1,[])
        
        
        return res
                
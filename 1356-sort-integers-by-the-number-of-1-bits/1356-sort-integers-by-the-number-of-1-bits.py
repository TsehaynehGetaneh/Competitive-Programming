class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        ans = []
        
        for num in arr:
            ans.append((num.bit_count(),num))
            
        ans.sort()
        
        res = []
        for count,num in ans:
            res.append(num)
            
        return res
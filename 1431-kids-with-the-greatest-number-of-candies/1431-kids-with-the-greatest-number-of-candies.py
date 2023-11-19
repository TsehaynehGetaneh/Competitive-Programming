class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_num = max(candies)
        
        res = []
        
        for num in candies:
            val = extraCandies + num
            
            if val >= max_num:
                res.append(True)
            else:
                res.append(False)
                
        return res
        
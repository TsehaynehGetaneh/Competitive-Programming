class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        no_candyType = len(set(candyType))
        half = len(candyType)//2
        
        
        if half <= no_candyType:
            return half
        
        if half > no_candyType:
            return no_candyType
        
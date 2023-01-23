class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        matrix = []
        
        if n*m == len(original):
            
            for i in range(0,len(original),n):
                row = original[i:i+n]
                matrix.append(row)
                
            
            return matrix
             
        else:
            return []
        
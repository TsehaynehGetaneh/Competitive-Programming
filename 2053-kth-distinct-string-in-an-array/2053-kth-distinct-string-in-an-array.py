class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)
        res = []
        
        for char in arr:
            if counter[char] == 1:
                res.append(char)
                
        return res[k-1] if (k-1) < len(res) else ""
        
        
        
        
        
        
        
class Solution:
    
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        min_val = float("inf")
        arr = [0] * k
        
        def find_min(idx):
            nonlocal min_val
            
            if idx >= len(cookies):
                max_val = max(arr)
                min_val = min(min_val,max_val)
                return
            
            if max(arr) >= min_val:
                return 
            
            for i in range(k):
                if arr[i] + cookies[idx] < min_val:
                    arr[i] += cookies[idx]
                    
                    find_min(idx+1)
                    arr[i] -= cookies[idx]
            
            
            
        cookies.sort(reverse=True)   
        find_min(0)
        
        return min_val
        
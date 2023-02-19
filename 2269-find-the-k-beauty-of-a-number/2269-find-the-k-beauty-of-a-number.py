class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num = str(num)
        count = 0
        
        i = 0
        j = k - 1
        while i<=j and j < len(num):
            val = int(num[i:j+1])
            
            if val != 0 and int(num)% val == 0:
                count += 1
                
            i += 1
            j += 1
            
        return count
            
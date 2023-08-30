class Solution:
    def maxLength(self, arr: List[str]) -> int:
        max_len = 0
        seq = [""]
        
        for string in arr:
            for s in seq:
                new_seq = s + string
                
                if len(new_seq) != len(set(new_seq)):
                    continue
                    
                seq.append(new_seq)
                
                max_len = max(max_len,len(new_seq))
              
        return max_len
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # hash the pattern and substring
        pattern_hash = 0
        match_hash = 0
        power = 0
        for i in range(len(needle)-1,-1,-1):
            if i < len(needle):
                hash_val_1 = ord(needle[i]) - ord("a") + 1
                pattern_hash += (hash_val_1 * 27**power)
                
            if i < len(haystack):
                hash_val_2 = ord(haystack[i]) - ord("a") + 1
                match_hash += (hash_val_2 * 27**power)
                
            power += 1
       
        # check first match
        if match_hash == pattern_hash:
            return 0
        
        for i in range(len(haystack)):
            # poll first operation
            hash_val_first = ord(haystack[i]) - ord("a") + 1
            poll_first = match_hash - (hash_val_first * 27**(len(needle)-1))
            match_hash = poll_first
            
            # add last operation
            if i+len(needle) < len(haystack):
                hash_val_last = ord(haystack[i+ len(needle)]) - ord("a") + 1
                add_last = match_hash*27 + (hash_val_last)
                match_hash = add_last
            
            if match_hash == pattern_hash:
                print(i,pattern_hash, match_hash)
                return i+1
            
        return -1
            
            
            
            
                
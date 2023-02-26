class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s = [*s]
        shift_val = [0] * len(s)
        
        for shift in shifts:
            start,end,direction = shift
            
            if direction == 1:
                shift_val[start] += 1
                if end + 1 < len(s):
                    shift_val[end+1] -= 1
            else:
                shift_val[start] -= 1
                if end + 1 < len(s):
                    shift_val[end+1] += 1
            
        
        for i in range(1,len(shift_val)):
            shift_val[i] += shift_val[i-1]
         
       
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        alphabet_dic = {}
        for i in range(len(alphabet)):
            alphabet_dic[alphabet[i]] = i
        
        print(len(s))
        for i in range(len(s)):
            val = shift_val[i] + alphabet_dic[s[i]]
            val %= len(alphabet)
            
            if val < 0:
                val = len(alphabet) - (-1*val)
            s[i] = alphabet[val]
            
            
        return "".join(s)
            
        
        
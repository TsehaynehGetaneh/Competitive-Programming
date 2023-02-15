class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        str_num = list(str(int("".join(list(map(str,num)))) + k))
        str_num = list(map(int,str_num))
        
        return str_num
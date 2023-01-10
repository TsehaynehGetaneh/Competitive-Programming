class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        output = []
        
        if num%3 == 0:
            middle_num = num//3
            output.extend([middle_num-1,middle_num,middle_num+1])
                
                
        return output
        
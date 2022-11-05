class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        givenNum= n
        count =0
        
        if n <=0:
            return False
        else:
            while n%3 == 0:
                n= n/3
                count +=1
            if 3**count == givenNum:
                return True
            else:
                return False
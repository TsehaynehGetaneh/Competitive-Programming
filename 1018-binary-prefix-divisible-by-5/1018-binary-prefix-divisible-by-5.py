class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        num_str = ""
        
        for num in nums:
            num_str += str(num)
            num = int(num_str,2)
            
            if num%5 == 0:
                ans.append(True)
                
            else:
                ans.append(False)
                
        return ans
        
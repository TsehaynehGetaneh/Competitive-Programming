class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        digit_sum = 0
        for num in nums:
            while num >= 10:
                remainder = num%10
                digit_sum += remainder
                
                num //= 10
                
            digit_sum += num
            
        
        return abs(element_sum - digit_sum)
class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        length = len(nums)
        
        for i in range(length):
            num = int(str(nums[i])[::-1])
            nums.append(num)
            
        return len(set(nums))
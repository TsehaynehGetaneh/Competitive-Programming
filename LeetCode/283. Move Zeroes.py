class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i == 0:
                zero = i
                nums.remove(zero)
                nums.append(zero)
                
        return nums
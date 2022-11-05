class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) -1
        j = len(nums) -1 -k
        if len(nums) ==1 or k ==0:
            return nums
        else:
            while j<i:
                rotateNum = nums.pop()
                nums.insert(0, rotateNum)
                i -=1
            
        return nums
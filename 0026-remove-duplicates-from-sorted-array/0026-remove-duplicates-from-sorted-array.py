class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return len(nums)
        else:
            i = 1
            j = len(nums) -1

            while i <= j:
                if nums[i] == nums[i-1]:
                    nums.pop(i)
                    j -=1
                else:
                    i +=1
                
        return len(nums)
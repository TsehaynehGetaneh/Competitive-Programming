class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return [nums[1], nums[0]]

        res = [0] * len(nums)
        if nums.count(0) > 1:
            return res
        
        if nums.count(0) == 1:
            temp = 0
            p = 1
            for i in range(len(nums)):
                if nums[i] == 0:
                    temp = i
                    continue
                p *= nums[i]
            res[temp] = p
        else:
            p = 1
            for i in range(1,len(nums)):
                p *= nums[i]
            for i in range(len(nums)):
                if i == 0:
                    res[i] = p
                else:
                    res[i] = p//nums[i] * nums[0]
        return res

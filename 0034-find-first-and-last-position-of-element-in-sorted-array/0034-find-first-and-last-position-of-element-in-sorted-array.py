class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1,-1]
        for i in range(len(nums)):
            if nums[i] == target and res[0] == -1:
                res[0] = i
            elif nums[i] == target:
                res[1] = i
        if res[0] != -1 and res[1] == -1:
            res[1] = res[0]
        return res 
        
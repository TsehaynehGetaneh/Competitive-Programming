class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key
        def mycmp(x,y):
            if x+y > y+x:
                return 1
            elif x == y:
                return 0
            else:
                return -1
        nums = [str(num) for num in nums]
        nums.sort(key = cmp_to_key(mycmp),reverse = True)
        res = ""
        for i in range(len(nums)):
            res += nums[i]
        if int(res) == 0:
            return '0'
        return res
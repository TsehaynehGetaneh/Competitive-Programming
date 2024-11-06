class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        d = defaultdict(int)

        for i in range(len(nums)):
            b = bin(nums[i])[2:].count("1")
            d[nums[i]] = b

        res = []
        left, right = 0, 0
        while left <= right and right < len(nums):
            sub_res = []
            while right < len(nums) and d[nums[left]] == d[nums[right]]:
                sub_res.append(nums[right])
                right += 1

            left = right
            res.append(sub_res)
        
        for i in range(1, len(res)):
            prev_max = max(res[i-1])
            curr_min = min(res[i])

            if prev_max > curr_min:
                return False

        return True
        
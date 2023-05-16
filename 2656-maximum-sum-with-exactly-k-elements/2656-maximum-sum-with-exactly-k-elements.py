class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        max_ = max(nums)
        count = 1
        
        ans = 0
        while count <=k:
            ans += (max_)
            count += 1
            max_ += 1
            
        return ans
        
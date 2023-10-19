class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        M = max(nums)
        m = min(nums)
        
        return max((M-k)-(m+k),0)
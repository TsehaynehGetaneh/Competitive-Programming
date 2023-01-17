class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        import itertools
        
        return itertools.permutations(nums)
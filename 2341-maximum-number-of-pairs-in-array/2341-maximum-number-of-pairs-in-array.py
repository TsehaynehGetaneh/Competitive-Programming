class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        from collections import Counter
        
        dic = Counter(nums)
        
        count_pairs = 0
        count_leftovers = 0
        
        for val in dic.values():
            count_pairs += val//2
            count_leftovers += val%2
            
        return [count_pairs, count_leftovers]
            
        
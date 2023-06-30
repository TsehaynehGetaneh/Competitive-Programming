class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counter = Counter(nums)
        summ = 0
        for key,val in counter.items():
            if val == 1:
                summ += key
        
        return summ
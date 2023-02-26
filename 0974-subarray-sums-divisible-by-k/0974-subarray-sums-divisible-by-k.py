class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        count = 0
        prefix_sum = 0
        
        for i in range(len(nums)):
            prefix_sum += nums[i]
            
            modulo = prefix_sum % k
            
            count += dic[modulo]
            
            dic[modulo] += 1
            
        return count
        
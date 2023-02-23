class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        curr_sum = 0
        count = 0
        
        for i in range(len(nums)):
            curr_sum += nums[i]
            
            # if curr_sum == k:
            #     count += 1
                
            if curr_sum -k in seen:
                count += seen[curr_sum-k]
                
            seen[curr_sum] += 1
            
        return count
      
                
            
        
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        prefix_sum = 0
        res = 0
        
        for i in range(len(nums)):
            prefix_sum += nums[i]
            
            if prefix_sum == k:
                res += 1
                
            if prefix_sum -k in seen:
                res += seen[prefix_sum-k]
                
            seen[prefix_sum] += 1
            
        return res
                
            
#         count = 0
#         sub_sum = 0
        
#         left = 0
#         for right in range(len(nums)):
#             sub_sum += nums[right]
            
#             while sub_sum >= k and left <= right:
#                 if sub_sum == k:
#                     sub_sum -= nums[left]
#                     count += 1
#                 else:
#                     sub_sum -= nums
#                 left -= 1
            
#             right += 1
            
#         return count
                
            
        
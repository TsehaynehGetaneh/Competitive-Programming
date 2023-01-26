class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dic = {}
        count = 0
        
        for i in range(len(nums)):
            # print(dic)
            if k-nums[i] in dic and dic[k-nums[i]] >0:
                count += 1
                dic[k-nums[i]] -= 1
                
            elif nums[i] not in dic:   
                dic[nums[i]] = 1
                
            elif nums[i] in dic:
                dic[nums[i]] += 1
            
        return count
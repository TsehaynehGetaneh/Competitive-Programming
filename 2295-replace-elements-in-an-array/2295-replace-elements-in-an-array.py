class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i
            
        for i in range(len(operations)):
            idx = dic[operations[i][0]]
            nums[idx] = operations[i][1]
            # update dic
            del dic[operations[i][0]]
            dic[operations[i][1]] = idx
            
        return nums
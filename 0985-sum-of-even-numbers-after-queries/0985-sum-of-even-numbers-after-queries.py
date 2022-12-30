class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        output = []
        
        evenSum = 0
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                evenSum += nums[i]
        
        
        for query in queries:
            beforeUpdate = nums[query[1]]
            nums[query[1]] += query[0]
            afterUpdate = nums[query[1]]
            
            if beforeUpdate%2 == 0 and afterUpdate%2 == 0:
                evenSum -= beforeUpdate
                evenSum += afterUpdate
                
                output.append(evenSum)
            elif beforeUpdate%2 != 0 and afterUpdate%2 == 0:
                evenSum += afterUpdate
                output.append(evenSum)
            elif beforeUpdate%2 == 0 and afterUpdate%2 != 0:
                evenSum -= beforeUpdate
                output.append(evenSum)
            else:
                output.append(evenSum)
            
        return output
        
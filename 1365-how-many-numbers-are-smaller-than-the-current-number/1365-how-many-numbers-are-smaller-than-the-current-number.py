class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_sort = sorted(nums)
        
        count = 0
        dic = {}
        
        for num in nums_sort:
            dic[num] = count
            count += 1
                
        print(dic)       
        output = []
        for num in nums:
            c = nums.count(num)
            output.append(dic[num]-c+1)
            
        return output
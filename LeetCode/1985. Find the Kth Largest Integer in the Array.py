class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        intList = []
        output = ''
        for i in range(len(nums)):
            num = int(nums[i])
            intList.append(num)
        intList.sort(reverse = True)
        
        for i in range(len(intList)):
            if (i + 1) == k:
                output += str(intList[i])
                
        return output
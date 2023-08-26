class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs,key=lambda x:x[1])
        count = 1
        val = pairs[0][1]
        
        for i in range(1,len(pairs)):
            if pairs[i][0] > val:
                count += 1
                val = pairs[i][1]
        
        return count
        
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        res = []
        d = {}
        for i in range(len(s)):
            d[s[i]] = i
        
        maxIndex = 0
        minIdx = -1
        for i in range(len(s)):
            maxIdx = d[s[i]]
            maxIndex = max(maxIndex, maxIdx)
            if i == maxIndex:
                res.append(i-minIdx)
                minIdx = i
        return res
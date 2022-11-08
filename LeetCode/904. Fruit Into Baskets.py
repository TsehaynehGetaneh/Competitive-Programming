class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        d = {}
        start = 0
        end = 0
        maxVal = 0
        while end < len(fruits):
            d[fruits[end]] = end
            if len(d) >= 3:
                minVal = min(d.values())
                del d[fruits[minVal]]
                start = minVal + 1
            maxVal = max(maxVal, end-start + 1)
            end += 1
        return maxVal
        

class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        output1 = sum(cardPoints[:k])
        i = k - 1
        j = len(cardPoints) - 1
        op = 0
        res = output1
        while i >= 0 and i <= j and op < k:
            output1 -= cardPoints[i]
            output1 += cardPoints[j]
            i -= 1
            j -= 1
            op += 1
            res = max(res, output1)
        return res

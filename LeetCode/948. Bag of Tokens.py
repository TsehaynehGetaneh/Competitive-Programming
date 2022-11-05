class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        tokens.sort()
        score = 0
        i = 0
        j = len(tokens) -1
        while i <= j:
            if power >= tokens[i]:
                score += 1
                power -= tokens[i]
                i +=1
            else:
                if score > 0 and i+1 <=j:
                    power += tokens[j]
                    score -= 1
                    j -= 1
                else:
                    break
        return score
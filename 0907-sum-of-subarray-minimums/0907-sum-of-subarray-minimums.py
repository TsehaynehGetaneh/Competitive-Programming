class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # more explanation on algomoster
        stack = []
        sum = 0
        curSum = 0
        for curValue in arr:
            curCount = 1
            while stack:
                if stack[-1][0] < curValue:
                    break
                value, count = stack.pop()
                curCount += count
                curSum -= value * count

            stack.append((curValue, curCount))
            curSum += curValue * curCount
            sum += curSum
        return sum%(10**9 + 7)
        
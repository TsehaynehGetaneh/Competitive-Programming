class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = sum(nums[:k])
        max_sum = summ
        j = 0

        for i in range(k, len(nums)):
            summ += nums[i] - nums[j]

            max_sum = max(max_sum, summ)
            j += 1

        return max_sum/k


        
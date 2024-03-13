class Solution:
    def pivotInteger(self, n: int) -> int:
        left, right = 1, n
        left_sum, right_sum = 0, 0
        
        while left <= right:
            if left_sum <= right_sum:
                left_sum += left
                left += 1
            else:
                right_sum += right
                right -= 1
       
        if left_sum > right_sum and left_sum - right == right_sum:
            return right
        
        if left_sum < right_sum and right_sum - left == left_sum:
            return left
        
        return -1
        
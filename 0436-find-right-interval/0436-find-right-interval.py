class Solution:
    def binary_search(self,intervals,interval,left,right):
        while left <= right:
            mid = (left+right)//2
            
            if intervals[mid][0] < interval[1]:
                left = mid + 1
            else:
                right = mid - 1
                
        return left
        
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        dic = {}
        for i in range(len(intervals)):
            dic[intervals[i][0]] = i
            
        
        intervals.sort()
        ans = [-1] * len(intervals)
        for interval in intervals:
            idx = dic[interval[0]]
            right_idx = self.binary_search(intervals,interval,0,len(intervals)-1)
            
            if right_idx < len(intervals):
                ans[idx] = dic[intervals[right_idx][0]]
            
        return ans
        
        
                
                
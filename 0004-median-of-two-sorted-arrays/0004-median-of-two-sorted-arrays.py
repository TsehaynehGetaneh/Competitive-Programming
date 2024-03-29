class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_arr = sorted(nums1 + nums2)
        n = len(merged_arr)
        
        if n%2 == 0:
            return (merged_arr[n//2]+merged_arr[n//2-1])/2
        
        return merged_arr[n//2]
        
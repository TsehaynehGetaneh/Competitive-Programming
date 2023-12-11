class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1 = set()
        ans2 = set()
        nums1_ = set(nums1)
        nums2_ = set(nums2)
        
        for num in nums1:
            if num not in ans1 and num not in nums2_:
                ans1.add(num)
                
        for num in nums2:
            if num not in ans2 and num not in nums1_:
                ans2.add(num)
                
        return [list(ans1), list(ans2)]
        
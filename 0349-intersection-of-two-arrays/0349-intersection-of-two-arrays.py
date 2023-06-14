class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_set = set(nums2)
        
        ans = set()
        res = []
        
        for num in nums1:
            if num not in ans and num in nums2_set:
                res.append(num)
                ans.add(num)
                
        return res
        
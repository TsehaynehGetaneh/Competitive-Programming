class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            target = nums1[i]
            for j in range(len(nums2)):
                if target == nums2[j]:
                    for k in range(j+1,len(nums2)):
                        if nums2[k] > target:
                            res[i] = nums2[k]
                            break
        return res
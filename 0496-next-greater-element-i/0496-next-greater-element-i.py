class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hash_map = {}
        
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                hash_map[stack.pop()] = nums2[i]

            stack.append(nums2[i])
                
        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            if nums1[i] in hash_map:
                res[i] = hash_map[nums1[i]]
                
        return res
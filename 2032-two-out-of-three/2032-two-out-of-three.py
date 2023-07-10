class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        all_nums = list(set(nums1+nums2+nums3))
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums3 = set(nums3)
        
        ans = []
        for num in all_nums:
            if (num in nums1 and num in nums2) or (num in nums1 and num in nums3) or (num in nums2 and num in nums3):
                ans.append(num)
                
        return ans
        
        
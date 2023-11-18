class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = Counter(nums1)
        d2 = Counter(nums2)
        
        intersection = {}
        for num in nums1:
            if num in d1 and num in d2:
                c1,c2 = d1[num], d2[num]
                if c1 < c2:
                    intersection[num] = c1
                else:
                    intersection[num] = c2
                
        res = []
        print(intersection)
        for key in intersection:
            res.extend([key]*intersection[key])
            
        return res
        
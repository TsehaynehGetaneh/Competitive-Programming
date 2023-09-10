class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0
        
        def merge(left,right):
            nonlocal count
            l,r = 0,0
            
            while l < len(left) and r < len(right):
                if left[l] > 2*right[r]:
                    count += len(left) - l
                    r += 1
                else:
                    l += 1
                    
            return sorted(left+right)
        
        def merge_sort(arr):
            if len(arr) == 1:
                return arr
            
            mid = len(arr)// 2
            
            return merge(merge_sort(arr[:mid]),merge_sort(arr[mid:]))
        
        
        merge_sort(nums)
        
        return count
        
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        data = set()
        res = []

        def backtrack(arr,path):
            if not arr and tuple(path) not in data:
                res.append(path)
                data.add(tuple(path))
                return 

            for i in range(len(arr)):
                backtrack(arr[:i] + arr[i+1:], path + [arr[i]])

        backtrack(nums, [])

        return res
        
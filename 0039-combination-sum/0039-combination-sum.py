class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        n = len(candidates)

        def backtrack(idx,path,sub_sum):
            if sub_sum == target:
                combinations.append(path)
                return 

            if sub_sum > target:
                return 

            for i in range(idx, n):
                backtrack(i, path + [candidates[i]], sub_sum + candidates[i])

        backtrack(0, [], 0)

        return combinations

        
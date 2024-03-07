class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = [str(i) for i in range(1,n+1)]
        permutations = []
        
        def backtrack(arr,path):
            if len(permutations) == k:
                return 

            if not arr:
                permutations.append(path)
                return 

            for i in range(len(arr)):
                backtrack(arr[:i] + arr[i+1:], path + [arr[i]])

        backtrack(res, [])
      
        return "".join(permutations[-1])
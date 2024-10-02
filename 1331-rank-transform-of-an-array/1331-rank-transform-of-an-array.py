class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr) == 0:
            return []

        # sort the array -> o(nlogn)
        new_arr = sorted(arr)
        h_map = {}
        h_map[new_arr[0]] = 1
        rank = 1

        # map each int to rank -> o(n)
        for i in range(1, len(new_arr)):
            if new_arr[i] == new_arr[i-1]:
                h_map[new_arr[i]] = rank
            else:
                rank += 1
                h_map[new_arr[i]] = rank

        # make the output array -> o(n)
        res = []
        for i in range(len(arr)):
            res.append(h_map[arr[i]])

        return res

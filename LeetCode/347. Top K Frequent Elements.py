class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter 
        dic = Counter(nums)
        sort_dic = sorted(dic.items(), reverse = True, key = lambda item : (item[1], item[0]))
        res = []
        idx = 0
        while idx < len(nums) and k > 0:
            res.append(int(sort_dic[idx][0]))
            idx += 1
            k -= 1
        return res

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        from collections import Counter
        dic = Counter(arr)
        sort_dic = sorted(dic.items(), key = lambda item :item[1], reverse = True)
        half = 0
        idx = 0
        while half < len(arr)//2:
            half += sort_dic[idx][1]
            idx += 1
        return idx

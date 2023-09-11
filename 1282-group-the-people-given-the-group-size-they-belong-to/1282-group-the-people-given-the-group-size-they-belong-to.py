class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic = defaultdict(list)
        res = []

        for i, size in enumerate(groupSizes):
            dic[size].append(i)
            if len(dic[size]) == size:
                res.append(dic[size])
                dic[size] = []

        return res

                
        
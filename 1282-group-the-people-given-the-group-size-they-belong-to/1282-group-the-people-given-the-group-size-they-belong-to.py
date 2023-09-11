class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic = defaultdict(list)
        res = []
        
        for i in range(len(groupSizes)):
            dic[groupSizes[i]].append(i)
     
        for key in dic:
            arr = dic[key]
            
            for i in range(0,len(arr),key):
                res.append(arr[i:i+key])
                
        return res
                
        
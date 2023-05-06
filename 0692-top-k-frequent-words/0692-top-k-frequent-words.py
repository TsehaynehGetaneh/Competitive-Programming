class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        arr = []
        
        for key in counter:
            arr.append((key,counter[key]))
         
        arr = sorted(arr,key = lambda x: (-x[1],x[0]))
        
        
        res = []
        for i in range(k):
            res.append(arr[i][0])
            
        return res
        
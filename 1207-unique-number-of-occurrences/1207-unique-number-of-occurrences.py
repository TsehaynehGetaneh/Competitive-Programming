class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        freq = []
        
        for val in counter.values():
            freq.append(val)
            
        freq.sort()
        
        for i in range(1,len(freq)):
            if freq[i-1] == freq[i]:
                return False
            
        return True
        
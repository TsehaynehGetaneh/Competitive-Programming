class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parents = [i for i in range(len(stones))]
        rank = [1] * len(stones)
        
        def find(x):
            if x == parents[x]:
                return x
            
            parents[x] = find(parents[x])
            
            return parents[x]
        
        def union(x,y):
            parx = find(x)
            pary = find(y)
            
            if parx != pary:
                if rank[parx] < rank[pary]:
                    parents[parx] = pary
                    
                elif rank[pary] < rank[parx]:
                    parents[pary] = parx
                    
                else:
                    parents[pary] = parx
                    rank[parx] += 1
                    
        for i in range(len(stones)):
            for j in range(i+1, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i, j)
        
        return len(stones) - len([i for i in range(len(stones)) if i == find(i)])
                
        
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        rep = {}
        rank = defaultdict(int)
        
        def find(x):
            if x not in rep:
                rep[x] = x
                return x
            
            if x == rep[x]:
                return x
            
            rep[x] = find(rep[x])
            
            return rep[x]
        
        def union(x,y):
            par_x = find(x)
            par_y = find(y)
            
            if rank[par_x] < rank[par_y]:
                rep[par_x] = par_y
            elif rank[par_y] < rank[par_x]:
                rep[par_y] = par_x
            else:
                rep[par_y] = par_x
                rank[par_x] += 1
                
        for a,b,c,d in equations:
            if b+c == "==":
                union(a,d)
               
        for a,b,c,d in equations:
            if b+c == "!=":
                if find(a) == find(d):
                    return False
                
        return True
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        queue = deque([])
        adj_list = defaultdict(list)
        indegree = defaultdict(int)
        res = []
        
        for i in range(len(recipes)):
            ingredients_ = ingredients[i]
            for ingredient in ingredients_:
                adj_list[ingredient].append(recipes[i])
                
                indegree[recipes[i]] += 1
                    
        for supply in supplies:
            queue.append(supply)
            
        
        while queue:
            node = queue.popleft()
            
            
            for child in adj_list[node]:
                
                indegree[child] -= 1
               
                if indegree[child] == 0:
                    queue.append(child)
                    res.append(child)
                    
        
        return res
                    
                    
                    
                    
                    
                    
                    
                    
                    
                
        
        
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        adj_list = defaultdict(list)
        for i in range(len(graph)):
            adj_list[i] = graph[i]
            
        
        ans = []
        def dfs(vertex,path):
            nonlocal ans
            if not adj_list[vertex]:
                return
            
            for num in adj_list[vertex]:
                if num == len(graph)-1:
                    cur_path = path + [num]
                    ans.append(cur_path)
                else:
                    dfs(num,path + [num])
                
        
        dfs(0,[0])
        # print(adj_list)
        return ans
            
        
        
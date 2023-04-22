class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for edge in edges:
            graph[edge[0]].append(graph[edge[1]])
            graph[edge[1]].append(graph[edge[0]])
            
        for key,val in graph.items():
            if len(val) == len(edges):
                return key
            
            
        
            
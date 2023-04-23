class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # vertices that are sinks(can't be destination) are answers
        vertices = set()
        destinations = set()
        
        for edge in edges:
            vertices.add(edge[0])
            vertices.add(edge[1])
            destinations.add(edge[1])
            
        return vertices - destinations
            
    
    
        
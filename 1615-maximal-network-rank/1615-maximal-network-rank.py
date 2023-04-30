class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for a,b in roads:
            graph[a].append(b)
            graph[b].append(a)
        # print(graph)    
        max_len = 0
        for i in range(n):
            for num in range(i+1,n):
                # print(i,num)
                len_ = len(graph[i]) + len(graph[num])

                if i in graph[num]:
                    len_ -= 1

                max_len = max(max_len,len_)
                
        return max_len
        
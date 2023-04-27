class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for i in range(len(rooms)):
            adj_list[i] = rooms[i]
        
        # BFS
        queue = deque([0])
        visited = set()
        visited.add(0)
        
        while queue:
            curr_room = queue.popleft()
            
            for child in adj_list[curr_room]:
                if child not in visited:
                    visited.add(child)
                    queue.append(child)
                    
        # check if all rooms are visited or not
        for i in range(len(rooms)):
            if i not in visited:
                return False
            
        return True
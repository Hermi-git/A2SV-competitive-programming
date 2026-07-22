class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque([0])
        visited = set([0])

        while q:
            key = q.popleft()
            for room in rooms[key]:
                if room not in visited:
                    q.append(room)
                    visited.add(room)
        
        if len(visited)< len(rooms):
            return False
        return True
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        def inbound(r, c):
            return 0 <= r < m and 0 <= c < n
        start = tuple(entrance)
        q = deque([start])
        visited = {start}
        path = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if (r, c) != start and (r == m-1 or c == n-1 or r == 0 or c == 0)  :
                    return path
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if inbound(nr, nc) and (nr, nc) not in visited and maze[nr][nc] == ".":
                        q.append((nr, nc))
                        visited.add((nr, nc))
            path += 1
        return -1


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead_set = set(deadends)
        if "0000" in dead_set:
            return -1
        def get_neighbors(state):
            neighs = []
            for i in range(4):
                digit = int(state[i])
                up = (digit + 1) % 10
                down = (digit - 1) % 10
                neighs.append(state[:i] + str(down) + state[i+1:])
                neighs.append(state[:i] + str(up) + state[i+1:])
            return neighs
        
        q = deque(["0000"])
        visited = set(["0000"])
        turns = 0
        while q:
            for _ in range(len(q)):
                lock = q.popleft()
                if lock == target:
                    return turns
                lock_neighbors = get_neighbors(lock)
                for neigh in lock_neighbors:
                    if neigh not in visited and neigh not in dead_set:
                        q.append(neigh)
                        visited.add(neigh)
            turns += 1
        
        return -1



                
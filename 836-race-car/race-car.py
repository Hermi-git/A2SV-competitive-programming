class Solution:
    def racecar(self, target: int) -> int:
        def get_neigh(pos, speed):
            up_s = speed * 2
            up_p = pos + speed
            if speed > 0:
                down_s = -1
            else:
                down_s = 1
            down_p = pos
            return [(up_p, up_s), (down_p, down_s)]
    
        q = deque([(0, 1, 0)])
        visited = {(0, 1)}

        while q:
            pos, spd, sequence = q.popleft()
            if pos == target:
                return sequence
            neighbors = get_neigh(pos, spd)
            for p, s in neighbors:
                if (p, s) not in visited:
                    q.append((p, s, sequence+1))
                    visited.add((p, s))
         

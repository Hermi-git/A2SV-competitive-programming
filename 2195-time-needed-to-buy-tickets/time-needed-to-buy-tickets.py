class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque(range(len(tickets)))
        count = 0 
        while tickets[k]:
            val = queue.popleft()
            tickets[val] -= 1

            count += 1
            if tickets[val] > 0:
                queue.append(val)
        return count
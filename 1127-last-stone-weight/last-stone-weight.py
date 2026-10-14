class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones_n = [-1 * weight for weight in stones]
        heap = stones_n
        heapq.heapify(heap)
        while len(heap) > 1:
            first = -1 * heapq.heappop(heap)
            second =  -1 * heapq.heappop(heap)
            if first != second:
                val = first - second
                heapq.heappush(heap, -1 * val)
        return -1 * heap[0] if heap else 0

class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        piles_n = [-1 * pile for pile in piles]
        heap = piles_n
        heapq.heapify(heap)
        for _ in range(k):
            val = -1 * (heapq.heappop(heap))
            item =  val - (val//2)
            heapq.heappush(heap, -1 * item)
        piles_p = [-1 * pile_n for pile_n in piles_n]
        return sum(piles_p)
        
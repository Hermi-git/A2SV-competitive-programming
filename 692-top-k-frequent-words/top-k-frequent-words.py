class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        word_count = Counter(words)
        heap = [(-val, key) for key, val in word_count.items()]
        heapq.heapify(heap)
        ans = []
        for _ in range(k):
            freq, val = heapq.heappop(heap)
            ans.append(val)
        return ans


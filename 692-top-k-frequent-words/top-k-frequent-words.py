class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        word_count = Counter(words)
        heap = [(-val, key) for key, val in word_count.items()]
        heapq.heapify(heap)
        ans = []
        count = []
        for _ in range(k):
            freq, val = heapq.heappop(heap)
            ans.append(val)
            count.append(freq)
        sorted_ans = sorted(ans)
        return sorted_ans if len(set(count))==1 else ans


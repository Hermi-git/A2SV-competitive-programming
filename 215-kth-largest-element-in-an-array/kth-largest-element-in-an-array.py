class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_heap = []
        for i in range(len(nums)):
            if i < k:
                heapq.heappush(min_heap, nums[i])
            else:
                if min_heap[0] < nums[i]:
                    heapq.heapreplace(min_heap, nums[i])
        return min_heap[0]
        
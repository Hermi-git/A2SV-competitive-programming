class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums_n = [-1 *num for num in nums]
        heap = nums_n
        heapq.heapify(heap)
        while k > 0:
            kth_largest = heapq.heappop(heap)
            k -= 1
        return -kth_largest
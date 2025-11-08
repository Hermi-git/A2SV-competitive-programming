class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        map = {0:-1}
        total = sum(nums)
        target = total % p
        running = 0
        if target == 0:
            return 0
        min_subarray = float('inf')
        for i in range(len(nums)):
            running += nums[i]
            prefix= running % p
            rem = (running - target + p) % p
            if rem in map:
                min_subarray = min(min_subarray, i - map[rem])
            map[prefix] = i
        return -1 if min_subarray == float('inf') or min_subarray == len(nums) else min_subarray

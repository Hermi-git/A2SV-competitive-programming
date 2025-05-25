class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        for i in range(n):
            val = start + 2 * i
            nums.append(val)
        bitmask = 0
        for num in nums:
            bitmask ^= num
        return bitmask
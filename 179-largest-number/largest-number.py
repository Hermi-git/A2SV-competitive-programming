from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a: int, b: int) -> int:
            if str(a) + str(b) > str(b) + str(a):
                return -1
            elif str(a) + str(b) < str(b) + str(a):
                return 1
            else:
                return 0
        sorted_nums = sorted(nums, key = cmp_to_key(compare))
        if sorted_nums[0] == 0:
            return '0'
        return ''.join(map(str, sorted_nums))
            
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for idx, num in enumerate(nums):
            d_num = target - num
            if d_num in mapping:
                return [mapping[d_num], idx]
            mapping[num] = idx
        return []
        
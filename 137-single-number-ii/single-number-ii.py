class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_count = Counter(nums)
        for num, ocr in nums_count.items():
            if ocr !=3:
                return num
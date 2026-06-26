class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        digit_sum =0
        str_nums = map(str, nums)
        for num in str_nums:
            for i in range(len(num)):
                digit_sum += int(num[i])
        return element_sum - digit_sum
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        str_nums = "".join(map(str, nums))
        separate_list = [int(num) for num in str_nums]
        return separate_list
from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = [str(num) for num in nums]
        def customSort(item1, item2):
            if item1 + item2 > item2 + item1:
                return -1  
            elif item1 + item2 < item2 + item1:
                return 1
            else:
                return 0
        
        n = len(nums_str)
        for i in range(n):
            for j in range(n - 1 - i):
                if customSort(nums_str[j], nums_str[j + 1]) == 1 :
                    nums_str[j], nums_str[j + 1] = nums_str[j + 1], nums_str[j]
        
        res = ''.join(nums_str)
        return '0' if res[0] == '0' else res





       
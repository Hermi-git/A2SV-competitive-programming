class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        h = sum(nums)
        res = None
        def validate(x):
            sub_count = 1
            summ = 0
            for num in nums:
                summ += num
                if summ > x:
                    sub_count += 1
                    summ = num
            return sub_count <= k              
        while l <= h:
            mid = (l+h)//2
            if validate(mid):
                res = mid
                h = mid-1
            else:
                l = mid+1
        return res





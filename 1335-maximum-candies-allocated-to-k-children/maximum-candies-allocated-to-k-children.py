class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        summ = sum(candies)
        if summ < k:
            return 0
        def validate(x):
            count = 0
            for candy in candies:
                count += (candy//x)
            return count >= k
        
        l = 1
        r = summ
        while l <= r:
            m = (l+r)//2
            if validate(m):
                l = m+1
            else:
                r = m-1
        return r


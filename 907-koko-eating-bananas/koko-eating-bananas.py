class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(k):
            hours = 0
            for pile in piles:
                hours += ceil(pile/k)
            return hours <= h

        l = 1
        r = max(piles)
        while l <= r:
            m = (l+r)//2
            if possible(m):
                r = m-1
            else:
                l = m+1
        return l
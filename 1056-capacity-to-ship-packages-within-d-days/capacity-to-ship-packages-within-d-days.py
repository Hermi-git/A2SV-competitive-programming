class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(n):
            day = 1
            total = 0

            for weight in weights:
                if total + weight > n:
                    day += 1
                    total = weight
                else:
                    total += weight
            return day <= days

        l = max(weights)
        r = sum(weights)
        while l <= r:
            m = (l+r)//2
            if canShip(m):
                r = m-1
            else:
                l = m+1
        return l

        
            
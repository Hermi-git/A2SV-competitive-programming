from bisect import bisect_left, bisect_right 
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def validate(radius):
            for house in houses:
                idx = bisect_left(heaters, house)

                left = abs(house - heaters[idx-1]) if idx > 0 else float('inf')
                right = abs(house - heaters[idx]) if idx < len(heaters) else float('inf')

                if min(left, right) > radius:
                    return False
            return True

        l = 0
        r = max(
            abs(max(houses)-min(heaters)),
            abs(max(heaters)-min(houses)))
        while l <= r:
            m = (l+r)//2
            if validate(m):
                r = m-1
            else:
                l = m+1
        return l
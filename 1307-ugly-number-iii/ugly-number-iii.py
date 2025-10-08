class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def lcm(a, b):
            return (a * b) // gcd(a, b)
        def pie(limit, a, b, c):
            single= limit//a + limit//b + limit//c
            double = limit//(lcm(a, b)) + limit//(lcm(a, c)) + limit//(lcm(b, c))
            triple = limit//(lcm(a, lcm(b, c)))

            total = single - double + triple
            return total

        left, right = 1, min(2 * 10 ** 9, n* min(a, b, c))
        while left <= right:
            mid = (left+right)//2
            count = pie(mid, a, b, c)
            if count > n:
                right = mid -1
            elif count < n:
                left = mid +1
            else:
                if mid % a == 0  or mid % b ==0 or mid %c ==0:
                    return mid
                else:
                    right = mid -1
                
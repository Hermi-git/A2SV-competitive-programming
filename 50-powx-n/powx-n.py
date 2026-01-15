class Solution:
    def myPow(self, x: float, n: int) -> float:
        def binary_exponent(base, exponent):
            result = 1
            while exponent > 0:
                if exponent & 1:
                    result *= base
                base *= base
                exponent >>= 1
            return result
        if n < 0:
            x = 1 / x       
            n = -n 
        return binary_exponent(x, n)
        
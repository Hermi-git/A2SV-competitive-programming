class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod  = 10**9 + 7
        def multiply(a, b, p):
            return ((a% p) * (b % p)) % p

        def binary_exponent(base, exponent):
            result = 1
            while exponent > 0:
                if exponent & 1:
                    result = multiply(base, result, mod)
                base = multiply(base, base, mod)
                exponent >>= 1
            return result
            
        even = n - (n//2)
        odd = n//2

        return (binary_exponent(5, even) * binary_exponent(4, odd)) % mod
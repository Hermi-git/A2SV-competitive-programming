class Solution:
    def mirrorDistance(self, n: int) -> int:
        n_str = str(n)
        reverse_n = int(n_str[::-1])
        return abs(n-reverse_n)
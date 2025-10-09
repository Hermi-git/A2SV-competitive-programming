class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest = min(num for num in nums)
        largest = max(num for num in nums)

        def greatest_common_divisor(a, b):
            if b == 0:
                return a
            return greatest_common_divisor(b, a%b)
        return greatest_common_divisor(smallest, largest)
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0 
        for i in range(len(nums)):
            g = nums[i]
            for j in range(i, len(nums)):
                g = math.gcd(g, nums[j])
                if g == k:
                    count += 1
        return count



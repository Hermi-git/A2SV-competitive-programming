class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        freqprev = Counter()
        freqnext = Counter(nums)

        special_triplets= 0
        for j in range(len(nums)):
            target = nums[j] * 2
            freqnext[nums[j]] -= 1
            cand = freqprev[target] * freqnext[target]
            special_triplets += cand
            freqprev[nums[j]] += 1
        return special_triplets % (10**9 + 7)
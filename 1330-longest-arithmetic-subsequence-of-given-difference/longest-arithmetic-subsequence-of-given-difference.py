class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        longest = 0
        for num in arr:
            prev = num - difference
            if prev  in dp:
                dp[num] = dp[prev]+1
            else:
                dp[num] = 1
            longest = max(longest, dp[num])
        return longest 

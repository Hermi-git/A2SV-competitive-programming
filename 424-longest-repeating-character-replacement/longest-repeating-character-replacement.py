class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_dict = defaultdict(int)
        max_len = 0
        l = 0
        for r in range(len(s)):
            s_dict[s[r]] +=1
            max_occr = max(s_dict.values())
            cur_len = r - l + 1

            if cur_len - max_occr > k:
                s_dict[s[l]] -= 1
                l += 1
                cur_len = r - l + 1

            max_len = max(max_len, cur_len)
        return max_len
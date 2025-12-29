class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_len = len(t)
        n = len(s)
        t_count = Counter(t)
        sub_range = [float("-inf"), float("inf")]
        left = 0
        count = 0
        for right in range(n):
            if s[right] in t_count:
                t_count[s[right]] -= 1
                if t_count[s[right]] >= 0:
                    count += 1
            while count == t_len:
                if right - left < sub_range[1] -sub_range[0]:
                    sub_range = [left, right]
                if s[left] in t_count:
                    t_count[s[left]] += 1
                    if t_count[s[left]] > 0:
                        count -= 1
                left += 1
        if sub_range[0] == float('-inf'):
            return ""
        else:
            return s[sub_range[0] : sub_range[1] + 1]
                

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = list(s)
        for i, ch in enumerate(s):
            ans[indices[i]] = ch
        return "".join(ans)
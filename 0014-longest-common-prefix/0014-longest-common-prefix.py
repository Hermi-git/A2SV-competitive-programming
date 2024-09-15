class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(len(s) for s in strs)

        res = ""
        for i in range(min_len):
            for s in strs:
                if strs[0][i] != s[i]:
                    return res
            res += strs[0][i]
                
        return res
        
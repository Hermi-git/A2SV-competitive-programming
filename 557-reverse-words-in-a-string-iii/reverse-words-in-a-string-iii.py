class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(" ")
        res = []
        for word in s_list:
            ans = word[::-1]
            res.append(ans)
        return " ".join(res)
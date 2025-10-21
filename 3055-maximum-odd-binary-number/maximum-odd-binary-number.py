class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s_list = [0] * len(s)
        count_1 = 0
        s_list[-1] = 1
        for i in range(len(s)):
            if s[i] == "1":
                count_1 += 1
        i = 0
        while count_1 > 1:
            s_list[i] = 1
            i += 1
            count_1 -= 1
        return ''.join(map(str, s_list))

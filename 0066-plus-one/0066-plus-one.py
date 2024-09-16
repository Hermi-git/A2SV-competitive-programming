class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d_str = ''.join(map(str, digits))
        d_num = int(d_str) +1

        d_new = str(d_num)
        res = [int(ch) for ch in d_new]
        return res
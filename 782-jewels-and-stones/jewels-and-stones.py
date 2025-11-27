class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = Counter(stones)
        count = 0
        for ch in jewels:
            if ch in s:
                count += s[ch]
        return count

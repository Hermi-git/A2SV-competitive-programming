class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = Counter(p)
        cur = Counter(s[:len(p)])
        anagrams = []
        if target == cur:
            anagrams.append(0)
        for r in range(len(s)-len(p)):
            cur[s[r+len(p)]] += 1
            cur[s[r]] -= 1
            if cur == target:
                anagrams.append(r+1)
        return anagrams

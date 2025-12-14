class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        cleaned = re.sub(r'[^a-zA-Z ]', ' ', paragraph).lower()
        p = cleaned.split()
        p_count = Counter(p)
        ans = (0, "")
        for letter in p_count:
            if letter not in banned:
                cur = (p_count[letter],  letter)
                ans = max(ans, cur)
        return ans[1]
        
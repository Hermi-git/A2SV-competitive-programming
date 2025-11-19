class Solution:
    def countVowels(self, word: str) -> int:
        v = {'a', 'e', 'i', 'o', 'u'}
        n = len(word)
        t = 0

        for i, ch in enumerate(word):
            if ch in v:
                sub = (i + 1) * (n - i)
                t += sub

        return t
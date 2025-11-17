class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set(["A", "E", "I", "O", "U", "a","e", "i", "o", "u"])
        vowel  = []
        for ch in s:
            if ch in vowels:
                vowel.append(ch)
        vowel.sort()
        t = []
        last = 0
        for ch in s:
            if ch not in vowels:
                t.append(ch)
            else:
                t.append(vowel[last])
                last += 1
        return "".join(t)
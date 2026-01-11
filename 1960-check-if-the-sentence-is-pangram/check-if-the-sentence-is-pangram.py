class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s_count = Counter(sentence)
        if len(s_count) < 26:
            return False
        return True
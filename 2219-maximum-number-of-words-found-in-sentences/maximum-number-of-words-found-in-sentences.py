class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        counter = [len(sentence.split()) for sentence in sentences]
        return max(counter)
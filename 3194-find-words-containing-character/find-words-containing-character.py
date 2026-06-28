class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for i in range(len(words)):
            idx = words[i].find(x)
            if idx != -1:
                ans.append(i)
        return ans

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = []
        i,j = 0, 0
        while i < len(word1) and j < len(word2):
            if word1[i:] >= word2[j:]:
                merge.append(word1[i])
                i += 1
            else:
                merge.append(word2[j])
                j += 1
        while i < len(word1):
            merge.append(word1[i])
            i += 1
        while j < len(word2):
            merge.append(word2[j])
            j += 1
        return ''.join(merge)
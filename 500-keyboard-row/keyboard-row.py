class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = set("qwertyuiop")
        second_row = set("asdfghjkl")
        third_row = set("zxcvbnm")


        result = []
        for word in words:
            word_lower = word.lower()
            count = 1
            row = first_row if word_lower[0] in first_row else second_row if word_lower[0] in second_row else third_row
            for i in range(1, len(word_lower)):
                if word_lower[i] in row:
                    count += 1
            if count == len(word_lower):
                result.append(word)

        return result
                

        
            
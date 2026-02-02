class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shift = [0] * len(s)
        for query in shifts:
            start, end, direction = query
            if direction == 0:
                shift[start] += -1
                if (end+1) < len(s):
                    shift[end+1] += 1
            if direction == 1:
                shift[start] += 1
                if (end+1) < len(s):
                    shift[end+1] += -1
        for  i in range(1, len(s)):
            shift[i] += shift[i-1]
        
        answer = ""
        for i in range(len(s)):
            letter = chr(((ord(s[i]) + shift[i] - ord('a'))%26) + ord('a'))
            answer += letter
        return answer
        


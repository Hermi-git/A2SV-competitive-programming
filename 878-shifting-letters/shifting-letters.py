class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        for i in range(len(s)-2, -1, -1):
            shifts[i] += shifts[i+1]
        
        answer = ""
        for j in range(len(s)):
            letter = chr(((ord(s[j]) + shifts[j] - ord("a"))%26)+ord("a"))
            answer += letter
        return answer
class Solution:
    def maximumLength(self, s: str) -> int:
        result = -1
        for length in range(1, len(s) + 1):
            substring_count = defaultdict(int)
            for i in range(len(s) - length + 1):
                substring = s[i:i + length]
                if all(char == substring[0] for char in substring): 
                    substring_count[substring] += 1

            
            for substring, count in substring_count.items():
                if count >= 3:
                    result = max(result, len(substring))

        return result


       
        
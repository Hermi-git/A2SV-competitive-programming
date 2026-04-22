class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(index, previous_value, count):
            if index == len(s):
                return count >= 2
            for i in range(index, len(s)):
                cur = int(s[index:i+1])
                if previous_value is None or previous_value - 1 == cur:
                    if dfs(i+1, int(cur), count+1):
                        return True
            return False

        return dfs(0, None, 0)
             
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        if ruleKey == "color":
            for t, c, n in items:
                if c == ruleValue:
                    count += 1
        elif ruleKey == "type":
            for t, c, n in items:
                if t == ruleValue:
                    count += 1
        elif ruleKey == "name":
            for t, c, n in items:
                if n == ruleValue:
                    count += 1
        return count


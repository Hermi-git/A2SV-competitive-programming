class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dict_s = {v:i for i, v in enumerate(s)}
        end = 0

        parti = [0]
        for i in range(len(s)):
            end = max(end, dict_s[s[i]])
            if i == end:
                parti.append(end - sum(parti) +1)
        
        
        return parti[1:]


        
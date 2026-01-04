class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        s_dict = {val:index for index, val in enumerate(s)}
        end = 0

        partitions = [0]
        for i in range(len(s)):
            end = max(end, s_dict[s[i]])
            if i == end:
                partitions.append(end - sum(partitions) +1)
        
        
        return partitions[1:]


        
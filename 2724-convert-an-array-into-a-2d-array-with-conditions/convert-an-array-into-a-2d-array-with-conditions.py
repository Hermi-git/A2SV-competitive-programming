class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        distnict = Counter(nums)
        max_freq = max(distnict.values())

        result = [[] for _ in range(max_freq)]
        for num, freq in distnict.items():
            for i in range(freq):
                result[i].append(num)
        return result 

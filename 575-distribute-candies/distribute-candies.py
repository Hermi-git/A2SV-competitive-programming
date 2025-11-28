class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        unique_types = set(candyType)
        n = len(candyType) // 2
        if(n > len(unique_types)):
            return len(unique_types)
        else:
            return n

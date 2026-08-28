class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for r in range(len(arr)-2):
            cand = arr[r:r+3]
            if all(x % 2 != 0 for x in cand):
                return True
        return False

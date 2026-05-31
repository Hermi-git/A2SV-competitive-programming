class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        degree = [0 for _ in range(n)]
        for r in range(n):
            for c in range(n):
                if matrix[r][c] == 1:
                    degree[r] += 1
        return degree
class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        teams = [0 for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] ==1:
                    teams[i] +=1
        return teams.index(max(teams))
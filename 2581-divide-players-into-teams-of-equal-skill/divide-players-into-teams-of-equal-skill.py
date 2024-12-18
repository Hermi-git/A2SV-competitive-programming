class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l, r = 0, len(skill) -1
        team = []
        while l < r:
            summ = skill[l] + skill[r]
            team.append(summ)
            l += 1
            r -= 1
        check_team =Counter(team)
        chemistry = 0
        if len(check_team) == 1:
            l, r = 0, len(skill) -1
            while l < r:
                chemistry += skill[l] * skill[r]
                l += 1
                r -= 1
            return chemistry
        return -1

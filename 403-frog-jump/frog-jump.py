class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if len(stones) >= 2 and stones[1] != 1:
            return False
        stone_indices = {stone: i for i, stone in enumerate(stones)}
        memo = {}

        def dp(index, last_jump):
     
            if index == len(stones) - 1:
                return True

            if (index, last_jump) in memo:
                return memo[(index, last_jump)]

            for jump in (last_jump - 1, last_jump, last_jump + 1):
                if jump <= 0:
                    continue
                next_pos = stones[index] + jump
                if next_pos in stone_indices:
                    next_index = stone_indices[next_pos]
                    if dp(next_index, jump):
                        memo[(index, last_jump)] = True
                        return True

            memo[(index, last_jump)] = False
            return False
        return dp(1, 1)

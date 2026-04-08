class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank_name = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        sorted_score = sorted(score, reverse=True)
        score_to_rank = {sorted_score[i]:i+1 for i in range(len(score))}
        ans = [0] * len(score)
        for i in range(len(score)):
            rank = score_to_rank[score[i]]
            if rank <= 3:
                ans[i] = rank_name[rank-1]
            else:
                ans[i] = str(rank)
        return ans
        

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        nums_count = Counter(nums)
        buckets = [[]for _ in range(n+1)]
        for key, value in nums_count.items():
            buckets[value].append(key)
        answer = []
        for i in range(len(buckets)-1, -1, -1):
            if buckets[i] == []:
                continue
            
            for j in range(len(buckets[i])):
                if len(answer) < k:
                    answer.append(buckets[i][j])
        return answer

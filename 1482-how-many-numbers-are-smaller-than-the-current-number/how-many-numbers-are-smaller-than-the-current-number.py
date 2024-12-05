class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_count =Counter(nums)
        answer = []
        for num in nums:
            count = 0
            for i, j in nums_count.items():
                if i < num:
                    count += j
            answer.append(count)
        return answer

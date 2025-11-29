class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        def find_last_occurrence_index(nums_list, target_element):
            for i in range(len(nums_list) - 1, -1, -1):
                if nums_list[i] == target_element:
                    return i
            return -1
        nums_count = Counter(nums)
        maxi = max(nums_count.values())
        candi = []
        for num in nums_count:
            if nums_count[num] == maxi:
                candi.append(num)
        mini = float('inf')
        for c in candi:
            start = nums.index(c)
            end = find_last_occurrence_index(nums, c)
            length = end - start +1
            mini = min(mini, length)
        return mini


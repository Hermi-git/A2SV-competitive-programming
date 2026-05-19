class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = set()
        i = 0
        while i < len(nums):
            val = nums[i]
            idx = val - 1
            if idx != i and nums[idx] == nums[i]:
                if nums[i] not in ans:
                    ans.add(nums[i])
                i += 1
            elif nums[idx] != nums[i]:
                nums[i], nums[idx] = nums[idx],nums[i]
            elif idx == i and nums[idx] == nums[i]:
                i += 1
        return list(ans)


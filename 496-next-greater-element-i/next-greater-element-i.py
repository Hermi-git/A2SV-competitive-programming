class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums1)
        mapp = {val:index for index, val in enumerate(nums1)}
        stack =[]
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                idx = stack.pop()
                if nums2[idx] in mapp:
                    result[mapp[nums2[idx]]] = nums2[i]
            stack.append(i)

        return result
            
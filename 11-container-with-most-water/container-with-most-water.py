class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        area = 0
        max_area = area
        while l < r:
            length = min(height[l], height[r])
            width = r - l
            area = length * width
            max_area = max(area, max_area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return max_area

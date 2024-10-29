class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height) 
        l, r = 0, n-1
        mr = height[r] 
        ml = height[l] 
        water = 0 
        while l < r: 
            if height[l] <= height[r]:
                l += 1
                ml = max(height[l], ml)
                w = ml - height[l]
                water += w
            else:
                r -= 1
                mr = max(height[r], mr)
                w = mr - height[r]
                water += w
        return water

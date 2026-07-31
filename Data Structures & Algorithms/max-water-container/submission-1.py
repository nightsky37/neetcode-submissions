class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            h = min(heights[l], heights[r])
            maxArea = max(maxArea, h * (r - l))
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea
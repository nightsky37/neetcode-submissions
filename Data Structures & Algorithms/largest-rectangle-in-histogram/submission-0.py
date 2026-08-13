class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stk = []
        heights.append(0)
        for R, h in enumerate(heights):
            L = R
            while stk and stk[-1][1] > h:
                L, prev_h = stk.pop()
                maxArea = max(maxArea, prev_h * (R - L))
            stk.append((L, h))

        return maxArea
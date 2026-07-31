class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total = 0
        for i in range(1, n - 1):
            l, r = i - 1, i + 1
            maxh_l = height[i]
            maxh_r = height[i]
            while l >= 0:
                maxh_l = max(maxh_l, height[l])
                l -= 1
            while r < n:
                maxh_r = max(maxh_r, height[r])
                r += 1
            # if height[l] <= height[i] or height[r] <= height[i]:
            #     continue
            print(i, min(maxh_l, maxh_r) - height[i])
            total += min(maxh_l, maxh_r) - height[i]
        
        return total
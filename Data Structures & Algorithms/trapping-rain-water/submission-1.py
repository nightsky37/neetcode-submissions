class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_max = []
        suffix_max = []
        curr_max = -1
        for n in height:
            curr_max = max(curr_max, n)
            prefix_max.append(curr_max)
           
        curr_max = -1
        for n in height[::-1]:
            curr_max = max(curr_max, n)
            suffix_max = [curr_max] + suffix_max

        total = 0
        for i in range(len(height)):
            print(height[i], prefix_max[i], suffix_max[i])
            if height[i] < prefix_max[i] and height[i] < suffix_max[i]:
                total += min(prefix_max[i], suffix_max[i]) - height[i]
        
        print(prefix_max)
        print(suffix_max)
        return total
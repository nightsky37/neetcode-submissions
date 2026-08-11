class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stk = []
        
        for current_day, current_temp in enumerate(temperatures):
            while stk and temperatures[stk[-1]] < current_temp:
                ans[stk[-1]] = current_day - stk[-1]
                stk.pop()
            stk.append(current_day)
        
        return ans
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stk = []
        result = [0] * n
        for i in range(n):
            while stk and temperatures[stk[-1]] < temperatures[i]:
                result[stk[-1]] = i - stk[-1]
                stk.pop()
            stk.append(i)
        return result

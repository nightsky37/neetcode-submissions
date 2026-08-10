class Solution:
    def is_integer(self, val):
        try:
            int(val)
            return True
        except ValueError:
            return False
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for t in tokens:
            if self.is_integer(t):
                # print(t)
                stk.append(int(t))
            else:
                # print(stk)
                if t == '+':
                    tmp = stk[-2] + stk[-1]
                if t == '-':
                    tmp = stk[-2] - stk[-1]
                if t == '*':
                    tmp = stk[-2] * stk[-1]
                if t == '/':
                    tmp = int(stk[-2] / stk[-1])
                stk.pop()
                stk.pop()
                stk.append(tmp)

        return stk[-1]
                
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        tmp = 0
        for t in tokens:
            if t == '+':
                a = stk.pop()
                b = stk.pop()
                tmp = b + a
                stk.append(tmp)
            elif t == '-':
                a = stk.pop()
                b = stk.pop()
                tmp = b - a
                stk.append(tmp)
            elif t == '*':
                a = stk.pop()
                b = stk.pop()
                tmp = b * a
                stk.append(tmp)
            elif t == '/':
                a = stk.pop()
                b = stk.pop()
                tmp = int(b / a)
                stk.append(tmp)
            else:
                stk.append(int(t))
        
        return stk[-1]
                
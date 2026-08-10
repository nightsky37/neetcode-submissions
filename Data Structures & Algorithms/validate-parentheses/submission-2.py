class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stk.append(c)
            if len(stk) == 0: return False
            if c == ')':
                if stk[-1] == '(':
                    stk.pop()
                else:
                    return False
            if c == ']':
                if stk[-1] == '[':
                    stk.pop()
                else:
                    return False
            if c == '}':
                if stk[-1] == '{':
                    stk.pop()
                else:
                    return False
        return True if len(stk) == 0 else False
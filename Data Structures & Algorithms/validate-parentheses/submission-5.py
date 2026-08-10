class Solution:
    def isValid(self, s: str) -> bool:
        close2open = {')':'(', ']':'[', '}':'{'}
        stk = []
        for c in s:
            if c in close2open:
                if stk and stk[-1] == close2open[c]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)
            
        return len(stk) == 0
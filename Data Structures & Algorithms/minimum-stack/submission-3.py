class MinStack:

    def __init__(self):
        self.stk = []
        self.minStk = []
        self.min = (1 << 31) - 1

    def push(self, val: int) -> None:
        self.stk.append(val)
        if val <= self.min:
            self.minStk.append(val)
            self.min = val

    def pop(self) -> None:
        if self.stk[-1] == self.minStk[-1]:
            self.minStk = self.minStk[:-1]
            if self.minStk:
                self.min = self.minStk[-1]
            else:
                self.min = (1 << 31) - 1
                
        self.stk = self.stk[:-1]

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minStk[-1]

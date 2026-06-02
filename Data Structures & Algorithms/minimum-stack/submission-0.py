class MinStack:

    def __init__(self):
        self.stack = []
    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack):
            self.stack.pop()

    def top(self) -> int:
        if len(self.stack): 
            return self.stack[-1]

    def getMin(self) -> int:
        tmp = self.stack.copy()
        if len(self.stack):
            mini = tmp[-1]
            while len(tmp):
                mini = min(mini,tmp[-1])
                tmp.pop()
            return mini
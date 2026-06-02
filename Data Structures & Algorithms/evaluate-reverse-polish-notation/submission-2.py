class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for k in tokens:
            if k in "+*-/":
                i = int(stack.pop())
                j = int(stack.pop())
                if k == '+':
                    stack.append(i+j)
                if k == '*':
                    stack.append(i*j)
                if k == '-':
                    stack.append(j-i)
                if k == '/':
                    stack.append(j/i)
            else:
                stack.append(k)
        return int(stack[0])
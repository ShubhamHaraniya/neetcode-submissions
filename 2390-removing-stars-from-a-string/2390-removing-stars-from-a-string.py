class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for a in list(s):
            if a == '*':
                stack.pop()
                continue
            stack.append(a)
        return "".join(stack)
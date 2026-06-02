class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        for i in range(len(s)):
            if s[i] in ['(','{','['] :
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] == closeToOpen[s[i]]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
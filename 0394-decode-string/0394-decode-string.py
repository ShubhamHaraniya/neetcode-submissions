class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                # Build the encoded string
                curr = ""
                while stack[-1] != '[':
                    curr = stack.pop() + curr

                stack.pop()  # Remove '['

                # Build the number (can have multiple digits)
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                stack.append(curr * int(num))

        return "".join(stack)
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        phone = {
                '2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz'
                }

        result = []
        
        def rec(idx,s):
            if idx == len(digits):
                result.append(s)
                return

            for i in range(len(phone[digits[idx]])):
                s += phone[digits[idx]][i]
                rec(idx+1,s)
                s = s[:-1]

        rec(0,"")

        return result
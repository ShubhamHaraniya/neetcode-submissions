class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        a = len(str2)
        b = len(str1)
        for i in range(min(a, b), 0, -1):
            if a % i == 0 and b % i == 0:
                if (str2 == str2[0:i]*(len(str2)//i)) and (str1 == str2[0:i]*(len(str1)//i)):
                    return str2[:i]
            else:
                continue
        return ""
        
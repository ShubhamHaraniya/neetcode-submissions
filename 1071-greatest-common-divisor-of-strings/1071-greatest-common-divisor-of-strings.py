class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # n = len(str2)
        # m = len(str1)
        # while n > 0:
        #     div = int(m / n)
        #     if div == 0:
        #         n = n // 2
        #         continue
        #     if (str2 == str2[0:n]*(len(str2)//n)) and (str1 == str2[0:n]*(len(str1)//n)):
        #         return str2[:n]
        #     else:
        #         n = n // 2
        # return ""
        a = len(str2)
        b = len(str1)
        for i in range(min(a, b), 0, -1):
            if a % i == 0 and b % i == 0:
                if (str2 == str2[0:i]*(len(str2)//i)) and (str1 == str2[0:i]*(len(str1)//i)):
                    return str2[:i]
            else:
                continue
        return ""
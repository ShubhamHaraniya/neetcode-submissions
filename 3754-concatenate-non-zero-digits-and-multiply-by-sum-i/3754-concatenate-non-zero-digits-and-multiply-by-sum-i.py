class Solution:
    def sumAndMultiply(self, n: int) -> int:
        out =  ""
        sum = 0
        for i in list(str(n)):
            if int(i) != 0:
                sum += int(i)
                out += i
        if len(out):
            return int(out)*sum
        else:
            return 0
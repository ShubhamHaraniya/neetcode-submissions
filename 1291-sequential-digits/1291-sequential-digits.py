class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        if low > high:
            return []

        out = []
        n = len(str(low))

        while n <= len(str(high)):
            start = "".join(str(i) for i in range(1, n + 1))

            while True:
                num = int(start)

                if low <= num <= high:
                    out.append(num)

                # Can't generate the next sequential number
                if start[-1] == '9':
                    break

                start = start[1:] + str(int(start[-1]) + 1)

            n += 1

        return out
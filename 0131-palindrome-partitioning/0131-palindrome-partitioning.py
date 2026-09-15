class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []

        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]

        def recurse(start: int, path: list[str]) -> None:
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                substr = s[start:end]
                if is_palindrome(substr):
                    path.append(substr)
                    recurse(end, path) 
                    path.pop()          
       
        recurse(0, [])

        return result
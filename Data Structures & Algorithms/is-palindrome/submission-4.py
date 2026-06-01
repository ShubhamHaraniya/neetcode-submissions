
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[^a-zA-Z0-9]", "", s.lower())
        low = 0
        high = len(s) - 1 
        while low < high:
            if s[low] != s[high]:
                return False
            else:
                low += 1
                high -= 1
        return True
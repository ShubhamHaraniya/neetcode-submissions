class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = r'[^a-zA-Z0-9]'
        cleaned_s = re.sub(pattern, '', s).lower()

        l,r = 0,len(cleaned_s) -1
        while l<=r:
            if cleaned_s[l] != cleaned_s[r]:
                return False
            l  += 1
            r -= 1
        return True
        
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # 1. Count vowels in the first window of length k
        current_vowels = sum(1 for ch in s[:k] if ch in vowels)
        max_vowels = current_vowels
        
        # 2. Slide the window across the rest of the string
        for i in range(k, len(s)):
            # Add incoming character
            if s[i] in vowels:
                current_vowels += 1
            # Remove outgoing character
            if s[i - k] in vowels:
                current_vowels -= 1
            
            # Keep the highest count seen so far
            if current_vowels > max_vowels:
                max_vowels = current_vowels
                if max_vowels == k:  # Early stop: cannot exceed window size
                    return k
        
        return max_vowels
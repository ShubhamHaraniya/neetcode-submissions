class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m,n  = len(word1),len(word2)
        merged = ""
        
        if m >  n :
            for i in range(n):
                merged += word1[i]
                merged += word2[i]
            merged = merged + word1[n:]
        elif m <  n :
            for i in range(m):
                merged += word1[i]
                merged += word2[i]
            merged = merged + word2[m:]
        else:
            for i in range(m):
                merged += word1[i]
                merged += word2[i]
        return merged
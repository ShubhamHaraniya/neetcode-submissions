class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)

        for i,candy in enumerate(candies):
            if candy + extraCandies >= max_candy:
                candies[i] = True
            else:
                candies[i] = False
        
        return candies
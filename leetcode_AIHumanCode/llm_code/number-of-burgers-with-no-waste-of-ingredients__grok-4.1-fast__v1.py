class Solution:
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        if tomatoSlices % 2:
            return []
        half_tomatoes = tomatoSlices // 2
        if half_tomatoes < cheeseSlices or half_tomatoes > cheeseSlices * 2:
            return []
        jumbo_count = half_tomatoes - cheeseSlices
        small_count = cheeseSlices * 2 - half_tomatoes
        return [jumbo_count, small_count]

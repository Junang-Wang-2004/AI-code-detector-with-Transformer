# Time:  O(n * r^2)
# Space: O(min(n * r^2, max_x * max_y))

# math, hash table
class Solution(object):
    def countLatticePoints(self, circles):
        """
        """
        lookup = set()
        for x, y, r in circles:
            for i in range(-r, r+1):
                for j in range(-r, r+1):
                    if i**2+j**2 <= r**2:
                        lookup.add(((x+i), (y+j)))
        return len(lookup)



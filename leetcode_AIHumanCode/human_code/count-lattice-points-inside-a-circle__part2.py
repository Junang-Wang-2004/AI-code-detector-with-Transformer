# Time:  O(n * max_x * max_y)
# Space: O(1)
# math
class Solution2(object):
    def countLatticePoints(self, circles):
        """
        """
        max_x = max(x+r for x, _, r in circles)
        max_y = max(y+r for _, y, r in circles)
        result = 0
        for i in range(max_x+1):
            for j in range(max_y+1):
                if any((i-x)**2+(j-y)**2 <= r**2 for x, y, r in circles):
                    result += 1
        return result

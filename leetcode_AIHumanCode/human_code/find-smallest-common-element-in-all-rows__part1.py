# Time:  O(m * n)
# Space: O(n)

class Solution(object):
    def smallestCommonElement(self, mat):
        """
        """
        # values could be duplicated in each row
        intersections = set(mat[0])
        for i in range(1, len(mat)):
            intersections &= set(mat[i])
            if not intersections:
                return -1
        return min(intersections)



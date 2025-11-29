# Time:  O(m * n)
# Space: O(1)

# array
class Solution(object):
    def areSimilar(self, mat, k):
        """
        """
        return all(row[i] == row[(i+k)%len(row)]for row in mat for i in range(len(row)))

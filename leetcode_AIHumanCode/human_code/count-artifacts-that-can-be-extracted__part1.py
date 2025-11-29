# Time:  O(a + d), a is the number of grids covered by artifacts, d is the size of dig
# Space: O(d)

# hash table
class Solution(object):
    def digArtifacts(self, n, artifacts, dig):
        """
        """
        lookup = set(map(tuple, dig))
        return sum(all((i, j) in lookup for i in range(r1, r2+1) for j in range(c1, c2+1)) for r1, c1, r2, c2 in artifacts)
    


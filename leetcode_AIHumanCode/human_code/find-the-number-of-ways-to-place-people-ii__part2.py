# Time:  O(n^3)
# Space: O(1)
# sort, array
class Solution2(object):
    def numberOfPairs(self, points):
        """
        """
        points.sort(key=lambda x: (x[0], -x[1]))
        return sum(all(not points[i][1] >= points[k][1] >= points[j][1] for k in range(i+1, j))
                   for i in range(len(points))
                   for j in range(i+1, len(points)) if points[i][1] >= points[j][1])
 

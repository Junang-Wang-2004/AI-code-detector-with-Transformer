# Time:  O(n^2)
# Space: O(1)

# sort, array
class Solution(object):
    def numberOfPairs(self, points):
        """
        """
        points.sort(key=lambda x: (x[0], -x[1]))
        result = 0
        for i in range(len(points)):
            y = float("-inf")
            for j in range(i+1, len(points)):
                if points[i][1] < points[j][1]:
                    continue
                if points[j][1] > y:
                    y = points[j][1]
                    result += 1
        return result



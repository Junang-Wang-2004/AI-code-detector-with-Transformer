# Time:  O(n^2)
# Space: O(1)
# sort, brute force
class Solution2(object):
    def maxRectangleArea(self, points):
        """
        """
        result = -1
        points.sort()
        for i in range(len(points)-3):
            if points[i][0] != points[i+1][0]:
                continue
            j = next((j for j in range(i+2, len(points)-1) if points[i][1] <= points[j][1] <= points[i+1][1]), len(points)-1)
            if j == len(points)-1 or not (points[j][0] == points[j+1][0] and points[i][1] == points[j][1] and points[i+1][1] == points[j+1][1]):
                continue
            result = max(result, (points[i+1][1]-points[i][1])*(points[j][0]-points[i][0]))
        return result
 

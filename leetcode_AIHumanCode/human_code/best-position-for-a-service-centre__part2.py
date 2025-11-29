# Time:  O(n * iter), iter is the number of iterations
# Space: O(1)
class Solution2(object):
    def getMinDistSum(self, positions):
        """
        """
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        EPS = 1e-6
        def dist(positions, p):
            return sum(((p[0]-x)**2 + (p[1]-y)**2)**0.5 for x, y in positions)
        
        median = [0.0, 0.0]
        median[0] = float(sum(x for x, _ in positions))/len(positions)
        median[1] = float(sum(y for _, y in positions))/len(positions)
        result = dist(positions, median)
        delta = float(max(max(positions, key=lambda x: x[0])[0],
                          max(positions, key=lambda x: x[1])[1])) - \
                float(min(min(positions, key=lambda x: x[0])[0],
                          min(positions, key=lambda x: x[1])[1]))
        while delta > EPS:
            for dx, dy in DIRECTIONS:
                new_median = [median[0] + delta*dx, median[1] + delta*dy]
                nd = dist(positions, new_median)
                if nd < result: 
                    result = nd 
                    median = new_median
                    break 
            else:
                delta /= 2.0
        return result 

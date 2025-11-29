# Time:  O(nlogn + (n * k * logn) * logs), s = side
# Space: O(n)
import bisect


# sort, binary search, greedy
class Solution4(object):
    def maxDistance(self, side, points, k):
        """
        """
        def binary_search_right(left, right, check):
            while left <= right:
                mid = left + (right-left)//2
                if not check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return right

        def check(d):
            for i in range(len(points)):
                j = i
                for _ in range(k-1):
                    j = bisect.bisect_left(p, p[j]+d, lo=j+1, hi=i+len(points))
                    if j == i+len(points):
                        break
                else:
                    if p[i+len(points)]-p[j] >= d:
                        return True
            return False

        p = []
        for x, y in points:
            if x == 0:
                p.append(0*side+y)
            elif y == side:
                p.append(1*side+x)
            elif x == side:
                p.append(2*side+(side-y))
            else:
                p.append(3*side+(side-x))
        p.sort()
        p += [x+4*side for x in p]
        return binary_search_right(1, 4*side//k, check)

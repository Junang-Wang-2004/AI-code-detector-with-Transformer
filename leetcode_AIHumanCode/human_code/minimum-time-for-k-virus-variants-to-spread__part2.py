# Time:  O(n^2 * logr), r is the sum of range x size and range y size
# Space: O(n)
import collections


# interview solution
class Solution2(object):
    def minDayskVariants(self, points, k):
        """
        """
        def add_rec(rec, intervals):
            x0, y0, x1, y1 = rec
            # add [y0, y1+1) by 1 in [x0, x1+1)
            intervals[x0][y0] += 1
            intervals[x0][y1+1] -= 1
            intervals[x1+1][y0] -= 1
            intervals[x1+1][y1+1] += 1

        def check(points, k, l):  # Time: O(n^2), Space: O(n)
            intervals = collections.defaultdict(lambda:collections.defaultdict(int))
            y_set = set()
            for x, y in points:
                add_rec([x-l, y-l, x+l, y+l], intervals)
                y_set.add(y-l)
                y_set.add(y+l+1)
            sorted_y = sorted(y_set)
            sorted_x = sorted(intervals.keys())
            count = collections.Counter()
            for x in sorted_x:  # line sweep
                for y, c in intervals[x].items():
                    count[y] += c
                cnt = 0
                for y in sorted_y:
                    cnt += count[y]
                    if cnt >= k:
                        return True
            return False
                
        points = [[x+y, x-y] for x, y in points]  # rotate
        min_x = min(points)[0]
        max_x = max(points)[0]
        min_y = min(points, key=lambda x: x[1])[1]
        max_y = max(points, key=lambda x: x[1])[1]
        left, right = 0, ((max_x-min_x)+(max_y-min_y)+1)//2
        while left <= right:
            mid = left + (right-left)//2
            if check(points, k, mid):
                right = mid-1
            else:
                left = mid+1
        return left

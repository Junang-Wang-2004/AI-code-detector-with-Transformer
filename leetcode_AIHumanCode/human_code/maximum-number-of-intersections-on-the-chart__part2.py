# Time:  O(nlogn)
# Space: O(n)
# sort, line sweep
class Solution2(object):
    def maxIntersectionCount(self, y):
        """
        """
        events = []
        for i in range(len(y)-1):
            # [y[i], y[i+1]) <=> [y[i], y[i+1]-0.5] <=> [2*y[i], 2*y[i+1]-1]
            left, right = 2*y[i], 2*y[i+1]+(-1 if y[i] < y[i+1] else +1)
            events.append((min(left, right), +1))
            events.append((max(left, right)+1, -1))
        # [y[i], y[i]] <=> [2*y[i], 2*y[i]]
        events.append((2*y[-1], +1))
        events.append((2*y[-1]+1, -1))
        events.sort()
        result = cnt = 0
        for _, c in events:
            cnt += c
            result = max(result, cnt)
        return result

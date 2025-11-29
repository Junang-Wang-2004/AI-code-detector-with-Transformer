class Solution:
    def isCovered(self, ranges, left, right):
        ranges.sort(key=lambda x: x[0])
        idx = 0
        pos = left
        while pos <= right:
            farthest = pos - 1
            while idx < len(ranges) and ranges[idx][0] <= pos:
                farthest = max(farthest, ranges[idx][1])
                idx += 1
            if farthest < pos:
                return False
            pos = farthest + 1
        return True

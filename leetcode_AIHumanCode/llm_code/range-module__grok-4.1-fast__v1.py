import bisect

class RangeModule:

    def __init__(self):
        self.ranges = []

    def addRange(self, left, right):
        i = 0
        n = len(self.ranges)
        prefix = []
        while i < n and self.ranges[i][1] < left:
            prefix.append(self.ranges[i])
            i += 1
        cl = left
        cr = right
        while i < n and self.ranges[i][0] <= cr:
            cl = min(cl, self.ranges[i][0])
            cr = max(cr, self.ranges[i][1])
            i += 1
        prefix.append((cl, cr))
        self.ranges = prefix + self.ranges[i:]

    def queryRange(self, left, right):
        pos = bisect.bisect_right(self.ranges, (left, float('inf'))) - 1
        return pos >= 0 and self.ranges[pos][1] >= right

    def removeRange(self, left, right):
        updated = []
        for curr in self.ranges:
            s, e = curr
            if e <= left or s >= right:
                updated.append(curr)
            else:
                if s < left:
                    updated.append((s, left))
                if right < e:
                    updated.append((right, e))
        self.ranges = updated

class Solution(object):
    def meetRequirement(self, n, lights, requirement):
        events = []
        for pos, rad in lights:
            left = max(0, pos - rad)
            right = min(n, pos + rad + 1)
            events.append((left, 1))
            events.append((right, -1))
        events.sort()
        count = 0
        active = 0
        idx = 0
        elen = len(events)
        m = len(requirement)
        p = 0
        while p < m:
            while idx < elen and events[idx][0] <= p:
                active += events[idx][1]
                idx += 1
            if active >= requirement[p]:
                count += 1
            p += 1
        return count

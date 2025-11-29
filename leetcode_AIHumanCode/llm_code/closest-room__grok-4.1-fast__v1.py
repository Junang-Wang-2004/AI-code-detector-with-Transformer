from sortedcontainers import SortedList

class Solution:
    def closestRoom(self, rooms, queries):
        rooms.sort(key=lambda x: -x[1])
        qlist = [(q[1], q[0], i) for i, q in enumerate(queries)]
        qlist.sort(reverse=True)
        sl = SortedList()
        res = [-1] * len(queries)
        j = 0
        for _, target, qi in qlist:
            while j < len(rooms) and rooms[j][1] >= _:
                sl.add(rooms[j][0])
                j += 1
            if not sl:
                continue
            idx = sl.bisect_right(target)
            closest = -1
            dist = float('inf')
            if idx < len(sl):
                d = abs(sl[idx] - target)
                if d < dist:
                    dist = d
                    closest = sl[idx]
            if idx > 0:
                d = abs(sl[idx - 1] - target)
                if d < dist:
                    dist = d
                    closest = sl[idx - 1]
                elif d == dist:
                    closest = min(closest, sl[idx - 1])
            res[qi] = closest
        return res

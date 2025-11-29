from sortedcontainers import SortedList
import collections

class C1:

    def __init__(self, a1):
        self.free_slots = SortedList()
        self.free_slots.add([0, a1])
        self.allocations = collections.defaultdict(list)

    def allocate(self, a1, a2):
        for v1 in self.free_slots:
            v2 = v1[0]
            v3 = v1[1]
            if v3 >= a1:
                self.free_slots.remove([v2, v3])
                self.allocations[a2].append([v2, a1])
                if v3 > a1:
                    self.free_slots.add([v2 + a1, v3 - a1])
                return v2
        return -1

    def free(self, a1):
        v1 = self.allocations.get(a1, [])
        if not v1:
            return 0
        v2 = sorted(v1, key=lambda x: x[0])
        v3 = []
        for v4, v5 in v2:
            if v3 and v3[-1][0] + v3[-1][1] == v4:
                v3[-1][1] += v5
            else:
                v3.append([v4, v5])
        v6 = sum((v5 for v7, v5 in v3))
        del self.allocations[a1]
        for v8 in v3:
            self.free_slots.add(v8)
            v9 = self.free_slots.bisect_left(v8)
            if v9 + 1 < len(self.free_slots) and self.free_slots[v9][0] + self.free_slots[v9][1] == self.free_slots[v9 + 1][0]:
                self.free_slots[v9][1] += self.free_slots[v9 + 1][1]
                del self.free_slots[v9 + 1]
            if v9 > 0 and self.free_slots[v9 - 1][0] + self.free_slots[v9 - 1][1] == self.free_slots[v9][0]:
                self.free_slots[v9 - 1][1] += self.free_slots[v9][1]
                del self.free_slots[v9]
        return v6

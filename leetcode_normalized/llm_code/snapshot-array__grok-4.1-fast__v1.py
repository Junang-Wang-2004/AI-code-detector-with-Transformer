import collections

class C1:

    def __init__(self, a1):
        self.records = collections.defaultdict(list)
        self.snap_cnt = 0

    def set(self, a1, a2):
        v1 = self.records[a1]
        if v1 and v1[-1][0] == self.snap_cnt:
            v1[-1][1] = a2
        else:
            v1.append([self.snap_cnt, a2])

    def snap(self):
        self.snap_cnt += 1
        return self.snap_cnt - 1

    def get(self, a1, a2):
        v1 = self.records[a1]
        v2, v3 = (0, len(v1) - 1)
        while v2 <= v3:
            v4 = (v2 + v3) // 2
            if v1[v4][0] <= a2:
                v2 = v4 + 1
            else:
                v3 = v4 - 1
        if v3 >= 0:
            return v1[v3][1]
        return 0

class C1:

    def __init__(self, a1=0, a2=0):
        self.start = a1
        self.end = a2

class C2:

    def employeeFreeTime(self, a1):
        v1 = []
        for v2 in a1:
            for v3 in v2:
                v1.append((v3.start, v3.end))
        if not v1:
            return []
        v1.sort(key=lambda x: x[0])
        v4 = []
        v5, v6 = v1[0]
        for v7, v8 in v1[1:]:
            if v7 <= v6:
                v6 = max(v6, v8)
            else:
                v4.append(C1(v5, v6))
                v5, v6 = (v7, v8)
        v4.append(C1(v5, v6))
        v9 = []
        for v10 in range(1, len(v4)):
            v11 = v4[v10 - 1].end
            v12 = v4[v10].start
            v9.append(C1(v11, v12))
        return v9

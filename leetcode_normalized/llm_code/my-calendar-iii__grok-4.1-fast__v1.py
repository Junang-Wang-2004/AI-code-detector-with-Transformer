class C1:

    def __init__(self):
        self.changes = []

    def book(self, a1, a2):
        self.changes.append((a1, 1))
        self.changes.append((a2, -1))
        self.changes.sort(key=lambda p: (p[0], p[1]))
        v1 = 0
        v2 = 0
        for v3, v4 in self.changes:
            v1 += v4
            if v1 > v2:
                v2 = v1
        return v2

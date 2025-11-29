class C1:

    def __init__(self):
        self.events = []
        self.doubles = []

    def book(self, a1, a2):
        for v1, v2 in self.doubles:
            if max(a1, v1) < min(a2, v2):
                return False
        for v3, v4 in self.events:
            v5 = max(a1, v3)
            v6 = min(a2, v4)
            if v5 < v6:
                self.doubles.append((v5, v6))
        self.events.append((a1, a2))
        return True

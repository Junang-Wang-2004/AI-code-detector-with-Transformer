class C1:

    def __init__(self):
        self.entries = []
        self.slices = {'Year': 4, 'Month': 7, 'Day': 10, 'Hour': 13, 'Minute': 16, 'Second': 19}

    def put(self, a1, a2):
        self.entries.append((a1, a2))

    def retrieve(self, a1, a2, a3):
        v1 = self.slices[a3]
        v2 = a1[:v1]
        v3 = a2[:v1]
        v4 = []
        for v5, v6 in self.entries:
            v7 = v6[:v1]
            if v2 <= v7 <= v3:
                v4.append(v5)
        v4.sort()
        return v4

class C1:

    def topStudents(self, a1, a2, a3, a4, a5):
        v1 = set(a1)
        v2 = set(a2)
        v3 = []
        for v4, v5 in zip(a4, a3):
            v6 = v5.split()
            v7 = 0
            for v8 in v6:
                if v8 in v1:
                    v7 += 3
                elif v8 in v2:
                    v7 -= 1
            v3.append((v7, v4))
        v3.sort(key=lambda pair: (-pair[0], pair[1]))
        return [v4 for v9, v4 in v3[:a5]]

class C1:

    def alertNames(self, a1, a2):

        def to_minutes(a1):
            v1, v2 = a1.split(':')
            return int(v1) * 60 + int(v2)
        v1 = {}
        for v2 in range(len(a1)):
            v3 = a1[v2]
            v4 = to_minutes(a2[v2])
            if v3 not in v1:
                v1[v3] = []
            v1[v3].append(v4)
        v5 = []
        for v3, v6 in v1.items():
            v6.sort()
            v7 = len(v6)
            v8 = False
            for v9 in range(v7 - 2):
                if v6[v9 + 2] - v6[v9] <= 60:
                    v8 = True
                    break
            if v8:
                v5.append(v3)
        v5.sort()
        return v5

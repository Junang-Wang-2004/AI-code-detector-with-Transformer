class C1:

    def expressiveWords(self, a1, a2):

        def parse_groups(a1):
            v1 = []
            v2 = 0
            v3 = len(a1)
            while v2 < v3:
                v4 = v2
                while v2 < v3 and a1[v2] == a1[v4]:
                    v2 += 1
                v1.append((a1[v4], v2 - v4))
            return v1
        v1 = parse_groups(a1)
        v2 = 0
        for v3 in a2:
            v4 = parse_groups(v3)
            if len(v1) != len(v4):
                continue
            v5 = True
            for (v6, v7), (v8, v9) in zip(v1, v4):
                if v6 != v8 or not (v7 == v9 or (v7 >= 3 and v7 >= v9)):
                    v5 = False
                    break
            if v5:
                v2 += 1
        return v2

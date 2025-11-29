class C1:

    def canReach(self, a1, a2):
        v1 = len(a1)
        v2 = set([a2])
        v3 = [a2]
        while v3:
            v4 = v3.pop()
            if a1[v4] == 0:
                return True
            v5 = a1[v4]
            for v6 in [v4 - v5, v4 + v5]:
                if 0 <= v6 < v1 and v6 not in v2:
                    v2.add(v6)
                    v3.append(v6)
        return False

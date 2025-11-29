class C1(object):

    def canChange(self, a1, a2):
        v1 = [(ch, idx) for v2, v3 in enumerate(a1) if v3 != '_']
        v4 = [(v3, v2) for v2, v3 in enumerate(a2) if v3 != '_']
        if len(v1) != len(v4):
            return False
        for (v5, v6), (v7, v8) in zip(v1, v4):
            if v5 != v7:
                return False
            if v5 == 'L' and v6 < v8 or (v5 == 'R' and v6 > v8):
                return False
        return True

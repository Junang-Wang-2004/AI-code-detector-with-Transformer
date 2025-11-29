class C1(object):

    def secondHighest(self, a1):
        v1 = [False] * 10
        for v2 in a1:
            if v2.isdigit():
                v1[int(v2)] = True
        v3 = -1
        v4 = -1
        for v5 in range(9, -1, -1):
            if v1[v5]:
                if v3 == -1:
                    v3 = v5
                else:
                    v4 = v5
                    break
        return v4

class C1(object):

    def lengthLongestPath(self, a1):
        v1 = [0]
        v2 = 0
        for v3 in a1.splitlines():
            v4 = 0
            v5 = 0
            while v5 < len(v3) and v3[v5] == '\t':
                v4 += 1
                v5 += 1
            v6 = len(v3) - v5
            while len(v1) > v4 + 1:
                v1.pop()
            v7 = v1[-1] + v6
            if '.' in v3[v5:]:
                v2 = max(v2, v7)
            else:
                v1.append(v7 + 1)
        return v2

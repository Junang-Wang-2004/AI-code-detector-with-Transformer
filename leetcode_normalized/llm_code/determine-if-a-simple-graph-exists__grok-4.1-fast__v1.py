class C1(object):

    def simpleGraphExists(self, a1):
        v1 = sum(a1)
        if v1 % 2:
            return False
        a1.sort(reverse=True)
        v2 = len(a1)
        v3 = 0
        v4 = v1
        v5 = v2 - 1
        v6 = 0
        for v7 in range(1, v2 + 1):
            v3 += a1[v7 - 1]
            v4 -= a1[v7 - 1]
            while v5 >= 0 and a1[v5] < v7:
                v6 += a1[v5]
                v5 -= 1
            v8 = max(0, v5 - v7 + 1)
            v9 = v7 * v8 + v6 if v8 > 0 else v4
            if v3 > v7 * (v7 - 1) + v9:
                return False
        return True

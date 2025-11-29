class C1(object):

    def largestGoodInteger(self, a1):
        if len(a1) < 3:
            return ''
        v1 = ''
        v2 = 0
        v3 = len(a1)
        v4 = 1
        while v4 <= v3:
            if v4 == v3 or a1[v4] != a1[v2]:
                if v4 - v2 >= 3:
                    v1 = max(v1, a1[v2])
                v2 = v4
            v4 += 1
        return v1 * 3

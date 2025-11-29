class C1(object):

    def minimumOperations(self, a1):
        v1 = 0
        v2 = 0
        v3 = len(a1) - 1
        v4 = a1[v2]
        v5 = a1[v3]
        while v2 < v3:
            if v4 < v5:
                v2 = v2 + 1
                v4 = v4 + a1[v2]
                v1 = v1 + 1
            elif v5 < v4:
                v3 = v3 - 1
                v5 = v5 + a1[v3]
                v1 = v1 + 1
            else:
                v2 = v2 + 1
                v3 = v3 - 1
                if v2 < v3:
                    v4 = a1[v2]
                    v5 = a1[v3]
        return v1

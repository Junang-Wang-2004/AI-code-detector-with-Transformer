class C1(object):

    def findPattern(self, a1, a2):
        if not a2 or not a1:
            return [-1, -1]
        v1, v2 = (len(a1), len(a1[0]))
        v3, v4 = (len(a2), len(a2[0]))

        def matches(a1, a2):
            v1 = {}
            v2 = set()
            for v3 in range(v3):
                for v4 in range(v4):
                    v5 = a1[a1 + v3][a2 + v4]
                    v6 = a2[v3][v4]
                    if v6.isdigit():
                        if int(v6) != v5:
                            return False
                    elif v6 not in v1:
                        if v5 in v2:
                            return False
                        v2.add(v5)
                        v1[v6] = v5
                    elif v1[v6] != v5:
                        return False
            return True
        for v5 in range(v1 - v3 + 1):
            for v6 in range(v2 - v4 + 1):
                if matches(v5, v6):
                    return [v5, v6]
        return [-1, -1]

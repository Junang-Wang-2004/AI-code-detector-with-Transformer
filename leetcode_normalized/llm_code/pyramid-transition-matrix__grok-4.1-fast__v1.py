class C1(object):

    def pyramidTransition(self, a1, a2):
        v1 = {}
        for v2 in a2:
            v3 = (v2[0], v2[1])
            v1.setdefault(v3, []).append(v2[2])
        v4 = {}

        def feasible(a1):
            if len(a1) == 1:
                return True
            if a1 in v4:
                return v4[a1]
            v1 = len(a1) - 1
            v2 = ['?'] * v1

            def extend(a1):
                if a1 == v1:
                    return feasible(''.join(v2))
                v1 = a1[a1:a1 + 2]
                for v2 in v1.get(v1, []):
                    v2[a1] = v2
                    if extend(a1 + 1):
                        return True
                return False
            v3 = extend(0)
            v4[a1] = v3
            return v3
        return feasible(a1)

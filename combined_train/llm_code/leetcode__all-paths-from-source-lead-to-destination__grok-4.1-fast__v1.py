class C1(object):

    def leadsToDestination(self, a1, a2, a3, a4):
        v1 = {}
        for v2, v3 in a2:
            if v2 not in v1:
                v1[v2] = []
            v1[v2].append(v3)
        v4 = set()
        v5 = set()

        def validate(a1):
            if a1 in v5:
                return True
            if a1 in v4:
                return False
            v4.add(a1)
            v1 = v1.get(a1, [])
            if len(v1) == 0 and a1 != a4:
                v4.remove(a1)
                return False
            for v2 in v1:
                if not validate(v2):
                    v4.remove(a1)
                    return False
            v4.remove(a1)
            v5.add(a1)
            return True
        return validate(a3)

class C1(object):

    def smallestCommonElement(self, a1):
        if not a1:
            return -1
        v1 = sorted(set(a1[0]))
        for v2 in a1[1:]:
            v3 = set(v2)
            v4 = [num for v5 in v1 if v5 in v3]
            v1 = v4
            if not v1:
                return -1
        return v1[0] if v1 else -1

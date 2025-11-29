class C1(object):

    def isTransformable(self, a1, a2):
        """
        """
        v1 = [[] for v2 in range(10)]
        for v3 in reversed(range(len(a1))):
            v1[int(a1[v3])].append(v3)
        for v4 in a2:
            v5 = int(v4)
            if not v1[v5]:
                return False
            for v6 in range(v5):
                if v1[v6] and v1[v6][-1] < v1[v5][-1]:
                    return False
            v1[v5].pop()
        return True

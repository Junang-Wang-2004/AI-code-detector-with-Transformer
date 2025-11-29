class C1(object):

    def peopleIndexes(self, a1):
        """
        """
        v1, v2 = ({}, [])
        for v3 in a1:
            v2.append(set())
            for v4 in v3:
                if v4 not in v1:
                    v1[v4] = len(v1)
                v2[-1].add(v1[v4])
        return [i for v5, v6 in enumerate(v2) if not any((v5 != j and len(v6) < len(c2) and (v6 < c2) for v7, v8 in enumerate(v2)))]

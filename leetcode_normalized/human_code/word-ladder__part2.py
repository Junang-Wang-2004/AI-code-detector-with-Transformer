class C1(object):

    def ladderLength(self, a1, a2, a3):
        """
        """
        v1 = set(a3)
        if a2 not in v1:
            return 0
        v2 = 2
        v3 = [a1]
        while v3:
            v4 = []
            for v5 in v3:
                for v6 in range(len(v5)):
                    for v7 in ascii_lowercase:
                        v8 = v5[:v6] + v7 + v5[v6 + 1:]
                        if v8 == a2:
                            return v2
                        if v8 in v1:
                            v1.remove(v8)
                            v4.append(v8)
            v3 = v4
            v2 += 1
        return 0

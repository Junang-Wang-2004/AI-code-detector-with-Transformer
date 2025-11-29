class C1(object):

    def fourSum(self, a1, a2):
        """
        """
        a1, v2, v3 = (sorted(a1), [], collections.defaultdict(list))
        for v4 in range(0, len(a1) - 1):
            for v5 in range(v4 + 1, len(a1)):
                v3[a1[v4] + a1[v5]].append([v4, v5])
        for v4 in list(v3.keys()):
            if a2 - v4 in v3:
                for v6 in v3[v4]:
                    for v7 in v3[a2 - v4]:
                        [v8, v9], [v10, v11] = (v6, v7)
                        if v8 is not v10 and v8 is not v11 and (v9 is not v10) and (v9 is not v11):
                            v12 = sorted([a1[v8], a1[v9], a1[v10], a1[v11]])
                            if v12 not in v2:
                                v2.append(v12)
        return sorted(v2)

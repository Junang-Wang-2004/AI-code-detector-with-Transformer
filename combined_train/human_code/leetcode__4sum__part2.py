class C1(object):

    def fourSum(self, a1, a2):
        """
        """
        a1, v2, v3 = (sorted(a1), [], collections.defaultdict(list))
        for v4 in range(0, len(a1) - 1):
            for v5 in range(v4 + 1, len(a1)):
                v6 = False
                for [v7, v8] in v3[a1[v4] + a1[v5]]:
                    if a1[v7] == a1[v4]:
                        v6 = True
                        break
                if not v6:
                    v3[a1[v4] + a1[v5]].append([v4, v5])
        v9 = {}
        for v10 in range(2, len(a1)):
            for v11 in range(v10 + 1, len(a1)):
                if a2 - a1[v10] - a1[v11] in v3:
                    for [v12, v13] in v3[a2 - a1[v10] - a1[v11]]:
                        if v13 < v10:
                            v14 = [a1[v12], a1[v13], a1[v10], a1[v11]]
                            v15 = ' '.join(str(v14))
                            if v15 not in v9:
                                v9[v15] = True
                                v2.append(v14)
        return v2

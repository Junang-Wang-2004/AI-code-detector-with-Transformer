class C1(object):

    def countSubTrees(self, a1, a2, a3):
        """
        """

        def iter_dfs(a1, a2, a3, a4, a5):
            v1 = [(1, (a3, a4, [0] * 26))]
            while v1:
                v2, v3 = v1.pop()
                if v2 == 1:
                    a3, a4, v6 = v3
                    v1.append((4, (a3, v6)))
                    v1.append((2, (a3, a4, reversed(a2[a3]), v6)))
                elif v2 == 2:
                    a3, a4, v7, v6 = v3
                    v8 = next(v7, None)
                    if not v8 or v8 == a4:
                        continue
                    v9 = [0] * 26
                    v1.append((2, (a3, a4, v7, v6)))
                    v1.append((3, (v9, v6)))
                    v1.append((1, (v8, a3, v9)))
                elif v2 == 3:
                    v9, v6 = v3
                    for v10 in range(len(v9)):
                        v6[v10] += v9[v10]
                else:
                    a3, v6 = v3
                    v6[ord(a1[a3]) - ord('a')] += 1
                    a5[a3] += v6[ord(a1[a3]) - ord('a')]
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = [0] * a1
        iter_dfs(a3, v1, 0, -1, v5)
        return v5

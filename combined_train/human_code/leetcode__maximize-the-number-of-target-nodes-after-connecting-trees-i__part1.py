class C1(object):

    def maxTargetNodes(self, a1, a2, a3):
        """
        """

        def centroid_decomposition(a1, a2):

            def dfs(a1):

                def find_subtree_size(a1, a2):
                    sizes[a1] = 1
                    for v1 in a1[a1]:
                        if v1 == a2 or lookup[v1]:
                            continue
                        sizes[a1] += find_subtree_size(v1, a1)
                    return sizes[a1]

                def find_centroid(a1, a2):
                    for v1 in a1[a1]:
                        if v1 == a2 or lookup[v1]:
                            continue
                        if sizes[v1] * 2 > n:
                            return find_centroid(v1, a1)
                    return a1

                def count(a1, a2, a3):
                    if a3 > a2:
                        return
                    if a3 - 1 == len(cnt):
                        cnt.append(0)
                    cnt[a3 - 1] += 1
                    for v1 in a1[a1]:
                        if v1 == a2 or lookup[v1]:
                            continue
                        count(v1, a1, a3 + 1)

                def update(a1, a2, a3):
                    if a3 > a2:
                        return
                    result[a1] += total[min(a2 - a3, len(total) - 1)] - curr[min(a2 - a3, len(curr) - 1)]
                    for v1 in a1[a1]:
                        if v1 == a2 or lookup[v1]:
                            continue
                        update(v1, a1, a3 + 1)
                find_subtree_size(a1, -1)
                v1 = sizes[a1]
                a1 = find_centroid(a1, -1)
                lookup[a1] = True
                v3 = 0
                for v4 in a1[a1]:
                    if lookup[v4]:
                        continue
                    v5 = []
                    count(v4, a1, 0 + 1)
                    prefix[v4].append(0)
                    for v6 in range(len(v5)):
                        prefix[v4].append(prefix[v4][-1] + v5[v6])
                    v3 = max(v3, len(v5))
                v7 = [1] * (v3 + 1)
                for v4 in a1[a1]:
                    if lookup[v4]:
                        continue
                    for v6 in range(len(v7)):
                        v7[v6] += prefix[v4][min(v6, len(prefix[v4]) - 1)]
                result[a1] += v7[min(a2, len(v7) - 1)]
                for v4 in a1[a1]:
                    if lookup[v4]:
                        continue
                    v8, prefix[v4] = (prefix[v4], [])
                    update(v4, a1, 0 + 1)
                for v4 in a1[a1]:
                    if lookup[v4]:
                        continue
                    dfs(v4)
            v1 = [0] * len(a1)
            v2 = [0] * len(a1)
            v3 = [False] * len(a1)
            v4 = [[] for v5 in range(len(a1))]
            if a2 >= 0:
                dfs(0)
            return v1

        def find_adj(a1):
            v1 = [[] for v2 in range(len(a1) + 1)]
            for v3, v4 in a1:
                v1[v3].append(v4)
                v1[v4].append(v3)
            return v1
        v1 = find_adj(a2)
        v2 = max(centroid_decomposition(v1, a3 - 1))
        v3 = find_adj(a1)
        return [v2 + x for v4 in centroid_decomposition(v3, a3)]

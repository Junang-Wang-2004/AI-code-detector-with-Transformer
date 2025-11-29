class C1(object):

    def numIslands2(self, a1, a2, a3):
        """
        """

        def node_id(a1, a2):
            return a1[0] * a2 + a1[1]

        def find_set(a1):
            if set[a1] != a1:
                set[a1] = find_set(set[a1])
            return set[a1]

        def union_set(a1, a2):
            v1, v2 = (find_set(a1), find_set(a2))
            set[min(v1, v2)] = max(v1, v2)
        v1 = []
        v2 = 0
        v3 = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        set = {}
        for v4 in a3:
            v5 = (v4[0], v4[1])
            set[node_id(v5, a2)] = node_id(v5, a2)
            v2 += 1
            for v6 in v3:
                v7 = (v4[0] + v6[0], v4[1] + v6[1])
                if 0 <= v7[0] < a1 and 0 <= v7[1] < a2 and (node_id(v7, a2) in set):
                    if find_set(node_id(v5, a2)) != find_set(node_id(v7, a2)):
                        union_set(node_id(v5, a2), node_id(v7, a2))
                        v2 -= 1
            v1.append(v2)
        return v1

import collections

class C1(object):

    def supersequences(self, a1):
        """
        """

        def f(a1):
            a1 = ord(a1) - ord('a')
            if char_to_int[a1] == -1:
                int_to_char[len(indegree)] = a1
                char_to_int[a1] = len(indegree)
                indegree.append(0)
            return char_to_int[a1]

        def topological_sort(a1):
            v1 = sum(a1)
            if v1 > ans[0]:
                return
            v2 = a1[:]
            v3 = indegree[:]
            v4 = [False] * len(a1)
            v5 = []
            for v6 in range(len(indegree)):
                if not v3[v6] or v2[v6] == 2:
                    v2[v6] -= 1
                    v4[v6] = True
                    v5.append(v6)
            while v5:
                v7 = []
                for v6 in v5:
                    for v8 in adj[v6]:
                        v3[v8] -= 1
                        if v3[v8]:
                            continue
                        v2[v8] -= 1
                        if v4[v8]:
                            continue
                        v4[v8] = True
                        v7.append(v8)
                v5 = v7
            if any(v2):
                return
            if v1 < ans[0]:
                ans[0] = v1
                ans[1][:] = []
            ans[1].append(a1)
        v1 = [[] for v2 in range(26)]
        v3, v4, v5 = ([-1] * 26, [0] * 26, [])
        for v6 in a1:
            v1[f(v6[0])].append(f(v6[1]))
            v5[f(v6[1])] += 1
        v7 = [float('inf'), []]
        for v8 in range(1 << len(v5)):
            topological_sort([2 if v8 & 1 << i else 1 for v9 in range(len(v5))])
        v10 = []
        for v11 in v7[1]:
            v12 = [0] * 26
            for v9, v13 in enumerate(v11):
                v12[v4[v9]] = v13
            v10.append(v12)
        return v10

from collections import deque

class C1:

    def countSubTrees(self, a1, a2, a3):
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = [[] for v2 in range(a1)]
        v6 = [False] * a1
        v7 = deque([0])
        v6[0] = True
        while v7:
            v8 = v7.popleft()
            for v9 in v1[v8]:
                if not v6[v9]:
                    v6[v9] = True
                    v5[v8].append(v9)
                    v7.append(v9)
        v10 = [0] * a1

        def postorder(a1):
            v1 = ord(a3[a1]) - ord('a')
            v2 = 1
            v3 = [0] * 26
            v3[v1] = 1
            for v4 in v5[a1]:
                v5 = postorder(v4)
                v2 += v5[v1]
                for v6 in range(26):
                    v3[v6] += v5[v6]
            v10[a1] = v2
            return v3
        postorder(0)
        return v10

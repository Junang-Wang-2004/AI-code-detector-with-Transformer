from collections import deque

class C1:

    def isBipartite(self, a1):
        v1 = len(a1)
        v2 = [-1] * v1
        for v3 in range(v1):
            if v2[v3] != -1:
                continue
            v4 = deque([v3])
            v2[v3] = 0
            while v4:
                v5 = v4.popleft()
                for v6 in a1[v5]:
                    if v2[v6] == -1:
                        v2[v6] = 1 - v2[v5]
                        v4.append(v6)
                    elif v2[v6] == v2[v5]:
                        return False
        return True

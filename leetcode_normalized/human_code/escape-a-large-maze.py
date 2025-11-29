import collections

class C1(object):

    def isEscapePossible(self, a1, a2, a3):
        """
        """
        v1, v2 = (10 ** 6, 10 ** 6)
        v3 = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def bfs(a1, a2, a3):
            v1 = len(a1) * (len(a1) - 1) // 2
            v2 = set([a2])
            if len(v2) > v1:
                return True
            v3 = collections.deque([a2])
            while v3:
                a2 = v3.popleft()
                if a2 == a3:
                    return True
                for v5 in v3:
                    v6, v7 = (a2[0] + v5[0], a2[1] + v5[1])
                    if not (0 <= v6 < v1 and 0 <= v7 < v2 and ((v6, v7) not in v2) and ((v6, v7) not in a1)):
                        continue
                    v2.add((v6, v7))
                    if len(v2) > v1:
                        return True
                    v3.append((v6, v7))
            return False
        return bfs(set(map(tuple, a1)), tuple(a2), tuple(a3)) and bfs(set(map(tuple, a1)), tuple(a3), tuple(a2))

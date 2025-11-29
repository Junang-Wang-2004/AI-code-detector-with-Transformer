import collections

class C1(object):

    def updateMatrix(self, a1):
        """
        """
        v1 = collections.deque()
        for v2 in range(len(a1)):
            for v3 in range(len(a1[0])):
                if a1[v2][v3] == 0:
                    v1.append((v2, v3))
                else:
                    a1[v2][v3] = float('inf')
        v4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while v1:
            v5 = v1.popleft()
            for dir in v4:
                v2, v3 = (v5[0] + dir[0], v5[1] + dir[1])
                if not (0 <= v2 < len(a1) and 0 <= v3 < len(a1[0]) and (a1[v2][v3] > a1[v5[0]][v5[1]] + 1)):
                    continue
                v1.append((v2, v3))
                a1[v2][v3] = a1[v5[0]][v5[1]] + 1
        return a1

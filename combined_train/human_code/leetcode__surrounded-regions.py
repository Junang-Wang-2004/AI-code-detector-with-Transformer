import collections

class C1(object):

    def solve(self, a1):
        """
        """
        if not a1:
            return
        v1 = collections.deque()
        for v2 in range(len(a1)):
            if a1[v2][0] == 'O':
                a1[v2][0] = 'V'
                v1.append((v2, 0))
            if a1[v2][len(a1[0]) - 1] == 'O':
                a1[v2][len(a1[0]) - 1] = 'V'
                v1.append((v2, len(a1[0]) - 1))
        for v3 in range(1, len(a1[0]) - 1):
            if a1[0][v3] == 'O':
                a1[0][v3] = 'V'
                v1.append((0, v3))
            if a1[len(a1) - 1][v3] == 'O':
                a1[len(a1) - 1][v3] = 'V'
                v1.append((len(a1) - 1, v3))
        while v1:
            v2, v3 = v1.popleft()
            for v4, v5 in [(v2 + 1, v3), (v2 - 1, v3), (v2, v3 + 1), (v2, v3 - 1)]:
                if 0 <= v4 < len(a1) and 0 <= v5 < len(a1[0]) and (a1[v4][v5] == 'O'):
                    a1[v4][v5] = 'V'
                    v1.append((v4, v5))
        for v2 in range(len(a1)):
            for v3 in range(len(a1[0])):
                if a1[v2][v3] != 'V':
                    a1[v2][v3] = 'X'
                else:
                    a1[v2][v3] = 'O'

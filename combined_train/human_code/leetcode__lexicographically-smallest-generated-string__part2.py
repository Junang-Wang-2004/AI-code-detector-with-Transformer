import collections

class C1(object):

    def generateString(self, a1, a2):
        """
        """

        def z_function(a1):
            v1 = [0] * len(a1)
            v2, v3 = (0, 0)
            for v4 in range(1, len(v1)):
                if v4 <= v3:
                    v1[v4] = min(v3 - v4 + 1, v1[v4 - v2])
                while v4 + v1[v4] < len(v1) and a1[v1[v4]] == a1[v4 + v1[v4]]:
                    v1[v4] += 1
                if v4 + v1[v4] - 1 > v3:
                    v2, v3 = (v4, v4 + v1[v4] - 1)
            return v1
        v1, v2 = (len(a1), len(a2))
        v3 = ['*'] * (v1 + v2 - 1)
        v4 = z_function(a2)
        v5 = -v2
        for v6, v7 in enumerate(a1):
            if v7 != 'T':
                continue
            v8 = v6 - v5
            if v8 < v2:
                if v4[v8] == v2 - v8:
                    v3[v5 + v2:v6 + v2] = a2[v2 - v8:]
                else:
                    return ''
            else:
                v3[v6:v6 + v2] = a2
            v5 = v6
        v9 = list(a2) + ['#'] + v3
        v10 = []
        for v6 in range(v2 + 1, len(v9)):
            if v9[v6] == '*':
                v9[v6] = 'a'
                v10.append(v6)
        v4 = z_function(v9)
        v11 = collections.deque()
        v6, v12 = (v2 + 1, 0)
        while v6 - (v2 + 1) < v1:
            while v11 and v11[0] < v6:
                v11.popleft()
            while v12 < len(v10) and v10[v12] <= v6 + (v2 - 1):
                v11.append(v10[v12])
                v12 += 1
            if a1[v6 - (v2 + 1)] == 'F' and v4[v6] == v2:
                if not v11:
                    return ''
                v9[v11[-1]] = 'b'
                v6 += v2
            else:
                v6 += 1
        return ''.join(v9[v2 + 1:])

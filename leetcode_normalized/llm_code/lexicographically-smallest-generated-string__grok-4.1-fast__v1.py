import collections

class C1(object):

    def generateString(self, a1, a2):
        v1, v2 = (len(a2), len(a1))
        v3 = self._zarray(a1)
        v4 = ['?'] * (v1 + v2 - 1)
        v5 = -v2
        for v6 in range(v1):
            if a2[v6] != 'T':
                continue
            v7 = v6 - v5
            if v7 < v2:
                if v3[v7] < v2 - v7:
                    return ''
                for v8 in range(v7):
                    v4[v6 + (v2 - v7) + v8] = a1[v2 - v7 + v8]
            else:
                for v8 in range(v2):
                    v4[v6 + v8] = a1[v8]
            v5 = v6
        v9 = []
        for v10 in range(v1 + v2 - 1):
            if v4[v10] == '?':
                v4[v10] = 'a'
                v9.append(v10)
        v11 = a1 + '$' + v4
        v12 = self._zarray(v11)
        v13 = collections.deque()
        v14 = 0
        v15 = v2 + 1
        while v15 < v2 + 1 + v1:
            v16 = v15 - v2 - 1
            while v13 and v13[0] < v15:
                v13.popleft()
            while v14 < len(v9) and v2 + 1 + v9[v14] <= v15 + v2 - 1:
                v13.append(v2 + 1 + v9[v14])
                v14 += 1
            if a2[v16] == 'F' and v12[v15] == v2:
                if not v13:
                    return ''
                v17 = v13[-1]
                v4[v17 - v2 - 1] = 'b'
                v15 += v2
            else:
                v15 += 1
        return ''.join(v4)

    def _zarray(self, a1):
        v1 = len(a1)
        v2 = [0] * v1
        v3 = v4 = 0
        for v5 in range(1, v1):
            if v5 < v4:
                v2[v5] = min(v4 - v5, v2[v5 - v3])
            while v5 + v2[v5] < v1 and a1[v2[v5]] == a1[v5 + v2[v5]]:
                v2[v5] += 1
            if v5 + v2[v5] > v4:
                v3 = v5
                v4 = v5 + v2[v5]
        return v2

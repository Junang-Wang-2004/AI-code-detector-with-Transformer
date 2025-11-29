import collections

class C1(object):

    def minExtraChar(self, a1, a2):
        v1 = len(a1)
        v2 = {}
        for v3 in a2:
            v4 = v2
            for v5 in v3:
                if v5 not in v4:
                    v4[v5] = {}
                v4 = v4[v5]
            v4['#'] = True
        v6 = v1 + 1
        v7 = [v6] * (v1 + 1)
        v7[0] = 0
        v8 = collections.deque([0])
        while v8:
            v9 = v8.popleft()
            v10 = v7[v9]
            v11 = v9 + 1
            if v11 <= v1 and v7[v11] > v10 + 1:
                v7[v11] = v10 + 1
                v8.append(v11)
            v4 = v2
            for v12 in range(v9, v1):
                v13 = a1[v12]
                if v13 not in v4:
                    break
                v4 = v4[v13]
                if '#' in v4:
                    v14 = v12 + 1
                    if v7[v14] > v10:
                        v7[v14] = v10
                        v8.appendleft(v14)
        return v7[v1]

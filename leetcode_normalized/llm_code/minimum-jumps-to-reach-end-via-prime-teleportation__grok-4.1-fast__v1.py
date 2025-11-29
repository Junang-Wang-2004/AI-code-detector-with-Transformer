import collections

def f1(a1):
    v1 = list(range(a1 + 1))
    v1[0] = v1[1] = 0
    for v2 in range(2, int(a1 ** 0.5) + 1):
        if v1[v2] == v2:
            for v3 in range(v2 * v2, a1 + 1, v2):
                if v1[v3] == v3:
                    v1[v3] = v2
    return v1
v1 = 10 ** 6
v2 = f1(v1)

class C1(object):

    def minJumps(self, a1):
        v1 = len(a1)
        v2 = collections.defaultdict(list)
        for v3, v4 in enumerate(a1):
            v5 = v4
            while v5 > 1:
                v6 = v2[v5]
                while v5 % v6 == 0:
                    v5 //= v6
                v2[v6].append(v3)
        v7 = [-1] * v1
        v7[0] = 0
        v8 = collections.deque([0])
        v9 = set()
        while v8:
            v10 = v8.popleft()
            if v10 == v1 - 1:
                return v7[v1 - 1]
            for v11 in (-1, 1):
                v12 = v10 + v11
                if 0 <= v12 < v1 and v7[v12] == -1:
                    v7[v12] = v7[v10] + 1
                    v8.append(v12)
            v13 = a1[v10]
            if v13 > 1 and v2[v13] == v13 and (v13 not in v9):
                v9.add(v13)
                for v14 in v2[v13]:
                    if v7[v14] == -1:
                        v7[v14] = v7[v10] + 1
                        v8.append(v14)
        return v7[v1 - 1]

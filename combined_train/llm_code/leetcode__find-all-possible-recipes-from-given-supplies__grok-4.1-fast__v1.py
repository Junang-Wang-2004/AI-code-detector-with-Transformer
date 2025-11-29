import collections

class C1(object):

    def findAllRecipes(self, a1, a2, a3):
        v1 = collections.defaultdict(list)
        v2 = {}
        v3 = set(a1)
        for v4, v5 in enumerate(a1):
            v2[v5] = len(a2[v4])
            for v6 in a2[v4]:
                v1[v6].append(v5)
        v7 = []
        v8 = collections.deque(a3)
        while v8:
            v9 = v8.popleft()
            if v9 in v3:
                v7.append(v9)
            for v10 in v1[v9]:
                v2[v10] -= 1
                if v2[v10] == 0:
                    v8.append(v10)
        return v7

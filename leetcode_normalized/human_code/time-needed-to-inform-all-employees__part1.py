import collections

class C1(object):

    def numOfMinutes(self, a1, a2, a3, a4):
        """
        """
        v1 = collections.defaultdict(list)
        for v2, v3 in enumerate(a3):
            if v3 != -1:
                v1[v3].append(v2)
        v4 = 0
        v5 = [(a2, 0)]
        while v5:
            v6, v7 = v5.pop()
            v7 += a4[v6]
            v4 = max(v4, v7)
            if v6 not in v1:
                continue
            for v8 in v1[v6]:
                v5.append((v8, v7))
        return v4

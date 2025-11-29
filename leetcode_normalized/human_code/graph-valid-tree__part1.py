import collections

class C1(object):

    def validTree(self, a1, a2):
        if len(a2) != a1 - 1:
            return False
        v1 = collections.defaultdict(list)
        for v2, v3 in a2:
            v1[v2].append(v3)
            v1[v3].append(v2)
        v4 = collections.deque([0])
        v5 = set([0])
        while v4:
            v6 = v4.popleft()
            for v7 in v1[v6]:
                if v7 not in v5:
                    v5.add(v7)
                    v4.append(v7)
        return len(v5) == a1

import collections

class C1(object):

    def minJumps(self, a1):
        """
        """
        v1 = collections.defaultdict(list)
        for v2, v3 in enumerate(a1):
            v1[v3].append(v2)
        v4 = collections.deque([(0, 0)])
        v5 = set([0])
        while v4:
            v6, v7 = v4.popleft()
            if v6 == len(a1) - 1:
                break
            v8 = set(v1[a1[v6]] + [v6 - 1, v6 + 1])
            v1[a1[v6]] = []
            for v9 in v8:
                if v9 in v5 or not 0 <= v9 < len(a1):
                    continue
                v5.add(v9)
                v4.append((v9, v7 + 1))
        return v7

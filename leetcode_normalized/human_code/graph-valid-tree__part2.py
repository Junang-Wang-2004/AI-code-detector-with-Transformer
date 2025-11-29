class C1(object):

    def validTree(self, a1, a2):
        v1 = [-1] * a1
        v2 = collections.defaultdict(list)
        for v3, v4 in a2:
            v2[v3].append(v4)
            v2[v4].append(v3)
        v5 = collections.deque([0])
        v6 = set([0])
        while v5:
            v7 = v5.popleft()
            for v8 in v2[v7]:
                if v8 != v1[v7]:
                    if v8 in v6:
                        return False
                    else:
                        v6.add(v8)
                        v1[v8] = v7
                        v5.append(v8)
        return len(v6) == a1

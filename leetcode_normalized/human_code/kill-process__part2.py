class C1(object):

    def killProcess(self, a1, a2, a3):
        """
        """

        def killAll(a1, a2, a3):
            a3.append(a1)
            for v1 in a2[a1]:
                killAll(v1, a2, a3)
        v1 = []
        v2 = collections.defaultdict(set)
        for v3 in range(len(a1)):
            v2[a2[v3]].add(a1[v3])
        v4 = collections.deque()
        v4.append(a3)
        while v4:
            v5 = v4.popleft()
            v1.append(v5)
            for v6 in v2[v5]:
                v4.append(v6)
        return v1

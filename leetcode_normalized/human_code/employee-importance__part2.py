class C1(object):

    def getImportance(self, a1, a2):
        """
        """
        v1, v2 = (0, collections.deque([a2]))
        while v2:
            v3 = v2.popleft()
            v4 = a1[v3 - 1]
            v1 += v4.importance
            for a2 in v4.subordinates:
                v2.append(a2)
        return v1

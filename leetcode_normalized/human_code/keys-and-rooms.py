class C1(object):

    def canVisitAllRooms(self, a1):
        """
        """
        v1 = set([0])
        v2 = [0]
        while v2:
            v3 = v2.pop()
            for v4 in a1[v3]:
                if v4 not in v1:
                    v1.add(v4)
                    if len(v1) == len(a1):
                        return True
                    v2.append(v4)
        return len(v1) == len(a1)

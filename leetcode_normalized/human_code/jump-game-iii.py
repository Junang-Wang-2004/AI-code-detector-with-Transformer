import collections

class C1(object):

    def canReach(self, a1, a2):
        """
        """
        v1, v2 = (collections.deque([a2]), set([a2]))
        while v1:
            v3 = v1.popleft()
            if not a1[v3]:
                return True
            for v4 in [v3 - a1[v3], v3 + a1[v3]]:
                if 0 <= v4 < len(a1) and v4 not in v2:
                    v2.add(v4)
                    v1.append(v4)
        return False
